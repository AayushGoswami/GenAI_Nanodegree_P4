# ChromaDB vector store
# core/db_handler.py

import os
import json
import chromadb
from typing import List, Dict
from sentence_transformers import SentenceTransformer

DATA_DIR = "data"
LISTINGS_PATH = os.path.join(DATA_DIR, "listings.json")
CHROMA_DIR = os.path.join(DATA_DIR, "chroma_store")

class DBHandler:
    def __init__(self):
        # ✅ Use the new PersistentClient
        self.client = chromadb.PersistentClient(path=CHROMA_DIR)
        self.model = SentenceTransformer("all-MiniLM-L6-v2")
        self.collection = self.client.get_or_create_collection("real_estate")

    def load_listings(self, path: str = LISTINGS_PATH) -> List[Dict]:
        with open(path, "r") as f:
            return json.load(f)

    def embed_text(self, text: str) -> List[float]:
        return self.model.encode(text).tolist()

    def populate_db(self, listings: List[Dict]):
        self.collection.delete('real_estate')
        self.collection = self.client.get_or_create_collection("real_estate")

        for idx, listing in enumerate(listings):
            listing_id = f"listing-{idx}"
            text_to_embed = listing["property_description"] + "\n" + listing["neighborhood_description"]
            embedding = self.embed_text(text_to_embed)

            self.collection.add(
                documents=[text_to_embed],
                metadatas=[listing],
                ids=[listing_id],
                embeddings=[embedding]
            )

    def query(self, query_text: str, top_k=3) -> List[Dict]:
        embedding = self.embed_text(query_text)
        results = self.collection.query(
            query_embeddings=[embedding],
            n_results=top_k,
            include=["documents", "metadatas"]
        )
        return results["metadatas"][0]
