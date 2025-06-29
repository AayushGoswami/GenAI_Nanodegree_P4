HomeMatch Notebook - README
===========================

Overview
--------
This notebook, `HomeMatch.ipynb`, demonstrates how to build an AI-powered real estate personalization app using GPT-3.5 (via OpenAI API) and ChromaDB. The app generates property listings, collects user preferences, semantically matches listings to those preferences, and rewrites the listings to highlight features important to the user.

Functionality
-------------
- **Generate Listings:** Uses GPT-3.5 to create 20 diverse real estate listings and saves them as both text and JSON.
- **Embed Listings:** Embeds the listings using a SentenceTransformer model and stores them in a ChromaDB vector database.
- **Collect Preferences:** Uses interactive widgets to collect buyer preferences.
- **Semantic Search:** Converts user preferences into an embedding and finds the top 5 most relevant listings using ChromaDB.
- **Personalize Listings:** Uses GPT-3.5 to rewrite the matched listings, emphasizing the buyer's preferences.
- **Display Results:** Shows the personalized listings and their details in a readable format.

How to Run
----------
1. **Install Dependencies:**
   - The notebook will install required packages automatically using `%pip install` at the start. Dependencies include: `langchain`, `openai`, `chromadb`, `sentence-transformers`, `ipywidgets`, `transformers`, and `tiktoken`.

2. **Set OpenAI API Key:**
   - You must provide your OpenAI (Vocareum) API key in the designated cell. Replace `<YOUR_API_KEY>` with your actual key.

3. **Run All Cells Sequentially:**
   - Start from the top and run each cell in order. The notebook is designed to be interactive, especially when collecting user preferences.
   - After entering your preferences and clicking the button, proceed to the semantic search and personalization steps.

Prerequisites & Dependencies
---------------------------
- **Python 3.8+**
- **Jupyter Notebook** or compatible environment (e.g., VS Code with Jupyter extension)
- **OpenAI API Key** (Vocareum endpoint)
- **Internet connection** (for model downloads and API calls)

Main Libraries Used:
- `openai` (for GPT-3.5)
- `langchain` (for LLM integration)
- `chromadb` (for vector database)
- `sentence-transformers` (for text embeddings)
- `ipywidgets` (for interactive UI)
- `transformers`, `tiktoken` (for tokenization and model support)

Notes
-----
- The notebook will create and use files such as `Listings.txt`, `listings.json`, and a `chroma_store` directory for the vector database.
- If you re-run the notebook, it will overwrite these files and reset the ChromaDB collection.
- Make sure to run the cell that sets the OpenAI API key before any cell that calls the LLM.

Troubleshooting
---------------
- If you encounter missing package errors, re-run the first cell to reinstall dependencies.
- Ensure your API key is valid and has access to the Vocareum endpoint.
- If widgets do not display, ensure you are running in a Jupyter-compatible environment with widget support enabled.

