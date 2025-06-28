# Semantic search logic
# core/search_engine.py

from typing import List, Dict
from core.db_handler import DBHandler
from core.llm_client import LLMClient

class SearchEngine:
    def __init__(self):
        self.db = DBHandler()
        self.llm = LLMClient()

    def search(self, preferences: str, top_k: int = 3) -> List[Dict]:
        return self.db.query(preferences, top_k=top_k)

    def personalize(self, listing: Dict, preferences: str) -> str:
        base_description = listing["Description"]
        prompt = f"""
You are a real estate agent personalizing property descriptions.
Given the buyer's preferences and the original listing, rewrite the listing to emphasize what matters to the buyer.

Buyer's Preferences:
{preferences}

Original Listing Description:
{base_description}

Neighborhood:
{listing['Neighborhood Description']}

Respond with the personalized listing only, no explanation.
"""
        return self.llm.ask(prompt)

    def search_and_personalize(self, preferences: str, top_k: int = 3) -> List[Dict]:
        results = self.search(preferences, top_k=top_k)
        personalized = []

        for listing in results:
            text = self.personalize(listing, preferences)
            personalized.append({
                "original": listing,
                "personalized": text
            })
        return personalized
