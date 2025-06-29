# HomeMatch: Personalized Real Estate Assistant

This project is part of the **BERTELSMANN next Gen Tech Booster Generative AI Nanodegree Program by Udacity**.

HomeMatch is an AI-powered real estate assistant that helps users find property listings tailored to their unique preferences. It leverages large language models (LLMs) for synthetic listing generation, semantic search, and personalized recommendations—all accessible through an interactive Streamlit web app.

## Table of Contents
- [Project Overview](#project-overview)
- [Features](#features)
- [Project Structure](#project-structure)
- [Setup Instructions](#setup-instructions)
- [How It Works](#how-it-works)
- [Example Usage](#example-usage)
- [Customization](#customization)
- [License](#license)

## Project Overview
This project allows users to:
- Answer a series of questions about their ideal home.
- Automatically generate synthetic property listings using LLMs.
- Use semantic search to match user preferences with the best listings.
- Receive personalized property descriptions that highlight what matters most to them.
- Preview and explore recommended listings in an interactive web interface.

The project is implemented in Python using Streamlit for the web app and ChromaDB for vector search.

## Features
- **Interactive Web App:** Answer questions and receive tailored property recommendations in your browser.
- **AI-Powered Listing Generation:** Create diverse, realistic property listings using LLMs.
- **Preference Parsing:** Collect and interpret user preferences through structured questions.
- **Semantic Search:** Find the best-matching listings using vector embeddings and ChromaDB.
- **Personalized Descriptions:** Listings are rewritten to emphasize features important to each user.

## Project Structure

```
homematch/
├── main.py                  # Entry point with Streamlit UI
├── core/
│   ├── llm_client.py        # GPT interface
│   ├── db_handler.py        # ChromaDB vector store
│   ├── listing_generator.py # Generates synthetic listings
│   ├── preference_parser.py # User input parser
│   └── search_engine.py     # Semantic search logic
├── data/
│   |── listings.json        # Stores generated listings
│   └── chroma_store         # ChromaDB vector store files
├── assets/                  # Optional: for future CLIP/image additions
├── requirements.txt
└── README.md
```

## Setup Instructions
1. **Clone the repository or download the project files.**
2. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```
3. **Set up OpenAI API credentials:**
   - The app is configured for Vocareum's OpenAI endpoint by default.
   - To use your own OpenAI API key, update the environment variables in `core/llm_client.py`.
    ```python
    os.environ["OPENAI_API_KEY"] = "YOUR_VOCAREUM_API_KEY"  # Replace with your actual API key
    ```
4. **Launch the app:**
   ```bash
   streamlit run main.py
   ```

## How It Works
- The user answers a series of questions about their dream home in the web app.
- The LLM generates a set of synthetic property listings.
- Listings are embedded using Sentence Transformers and stored in ChromaDB.
- The app uses semantic search to find the most relevant listings based on user preferences.
- The LLM rewrites each listing to emphasize features important to the user.
- The app displays the top matching listings with personalized descriptions.

## Example Usage
- Find a family-friendly home with a large backyard and good schools nearby.
- Search for a modern apartment in the city center with a gym and pet-friendly policies.
- Discover unique properties that match your specific lifestyle needs.

Example workflow in the app:
1. Launch the app and answer the preference questions.
2. Click "Find Matching Homes" to generate recommendations.
3. Browse the personalized listings and explore property details.

## Customization
- **Add More Questions:** Edit `core/preference_parser.py` to customize the user questionnaire.
- **Change LLM Model:** Update the model in `core/llm_client.py` as needed.
- **Expand Listing Fields:** Modify `core/listing_generator.py` to generate additional property details.
- **Add Example Listings:** Place new example data in `data/listings.json` for experimentation.

## License
See [LICENSE](../LICENSE) for details.
