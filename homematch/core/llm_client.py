# GPT interface
# core/llm_client.py

import os
from langchain.chat_models import ChatOpenAI
from langchain.schema import HumanMessage

# Set API key and base URL for Vocareum OpenAI endpoint
os.environ["OPENAI_API_KEY"] = "YOUR_VOCAREUM_API_KEY"  # Replace with your actual API key
os.environ["OPENAI_API_BASE"] = "https://openai.vocareum.com/v1"

class LLMClient:
    def __init__(self, temperature: float = 0.7):
        self.llm = ChatOpenAI(
            model_name="gpt-3.5-turbo",
            temperature=temperature
        )

    def ask(self, prompt: str) -> str:
        response = self.llm([HumanMessage(content=prompt)])
        return response.content
