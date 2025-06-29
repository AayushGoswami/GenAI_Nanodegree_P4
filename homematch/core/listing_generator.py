# Generates synthetic listings
# core/listing_generator.py

import os
import json
from typing import List, Dict
from core.llm_client import LLMClient

DATA_DIR = "data"
LISTINGS_PATH = os.path.join(DATA_DIR, "listings.json")

LISTING_GEN_PROMPT = """
Generate {num} diverse real estate property listings. Each listing must include:
- Neighborhood name
- Price (in USD)
- Bedrooms
- Bathrooms
- House Size (in sqft)
- Property Description (3-5 sentences)
- Neighborhood Description (2-4 sentences)

Use realistic details. Output in JSON list format.
"""

class ListingGenerator:
    def __init__(self):
        self.llm = LLMClient()

    def generate_listings(self, num=100) -> List[Dict]:
        prompt = LISTING_GEN_PROMPT.format(num=num)
        raw = self.llm.ask(prompt)

        # Basic cleanup (LLMs sometimes wrap output in markdown)
        try:
            listings = json.loads(raw.strip("```json\n").strip("```"))
        except Exception as e:
            raise ValueError("Failed to parse LLM response as JSON.") from e
        
        return listings

    def save_listings(self, listings: List[Dict], path: str = LISTINGS_PATH):
        os.makedirs(DATA_DIR, exist_ok=True)
        with open(path, "w") as f:
            json.dump(listings, f, indent=2)

    def generate_and_save(self):
        listings = self.generate_listings()
        self.save_listings(listings)
        return listings
