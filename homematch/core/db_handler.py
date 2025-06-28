# ChromaDB vector store
# core/db_handler.py

import os
import json
import chromadb
from typing import List, Dict
from chromadb.config import Settings
from sentence_transformers import SentenceTransformer

DATA_DIR = "data"
LISTINGS_PATH = os.path.join(DATA_DIR, "listings.json")
CHROMA_DIR = os.path.join(DATA_DIR, "chroma_store")

class DBHandler:
    def __init__(self):
        self.client = chromadb.Client(Settings(
            chroma_db_impl="duckdb+parquet",
            persist_directory=CHROMA_DIR
        ))
        self.model = SentenceTransformer("all-MiniLM-L6-v2")
        self.collection = self.client.get_or_create_collection("real_estate")

    def load_listings(self, path: str = LISTINGS_PATH) -> List[Dict]:
        with open(path, "r") as f:
            return json.load(f)

    def embed_text(self, text: str) -> List[float]:
        return self.model.encode(text).tolist()

    def populate_db(self, listings: List[Dict]):
        self.collection.delete(where={})  # Clear previous entries

        for idx, listing in enumerate(listings):
            listing_id = f"listing-{idx}"
            text_to_embed = listing["Description"] + "\n" + listing["Neighborhood Description"]
            embedding = self.embed_text(text_to_embed)

            self.collection.add(
                documents=[text_to_embed],
                metadatas=[listing],
                ids=[listing_id],
                embeddings=[embedding]
            )
        self.client.persist()

    def query(self, query_text: str, top_k=3) -> List[Dict]:
        embedding = self.embed_text(query_text)
        results = self.collection.query(
            query_embeddings=[embedding],
            n_results=top_k,
            include=["documents", "metadatas"]
        )
        return results["metadatas"][0]
