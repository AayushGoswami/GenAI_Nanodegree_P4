# Entry point with Streamlit UI
# main.py

import streamlit as st
from core.listing_generator import ListingGenerator
from core.db_handler import DBHandler
from core.preference_parser import PreferenceParser
from core.search_engine import SearchEngine

st.set_page_config(page_title="🏡 HomeMatch", layout="wide")
st.title("🏠 HomeMatch — Your Personalized Real Estate Assistant")

# Load or generate listings
@st.cache_data
def prepare_data():
    generator = ListingGenerator()
    listings = generator.generate_and_save()
    db = DBHandler()
    db.populate_db(listings)
    return listings

with st.spinner("Preparing listings and vector database..."):
    listings = prepare_data()

# Collect buyer preferences
parser = PreferenceParser()
answers = parser.ask_questions()

if st.button("🔍 Find Matching Homes"):
    if any(not ans.strip() for ans in answers):
        st.warning("Please fill out all preference fields.")
    else:
        preferences = parser.compile_preferences(answers)
        engine = SearchEngine()
        with st.spinner("Matching and personalizing listings..."):
            results = engine.search_and_personalize(preferences)

        st.subheader("🏡 Personalized Listings Just for You:")
        for idx, r in enumerate(results, 1):
            with st.expander(f"🏘️ Listing #{idx}", expanded=True):
                st.markdown("**Personalized Description:**")
                st.write(r["personalized"])
                st.markdown("---")
                st.markdown("**Original Listing Details:**")
                for key in ["neighborhood", "price", "bedrooms", "bathrooms", "house_size"]:
                    st.write(f"**{key.capitalize().replace('_', ' ')}:** {r['original'].get(key, 'N/A')}")
