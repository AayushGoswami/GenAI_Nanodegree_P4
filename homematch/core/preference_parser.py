# User input parser
# core/preference_parser.py

from typing import List

class PreferenceParser:
    def __init__(self):
        # Default set of structured questions
        self.questions = [
            "How big do you want your house to be?",
            "What are 3 most important things for you in choosing this property?",
            "Which amenities would you like?",
            "Which transportation options are important to you?",
            "How urban do you want your neighborhood to be?",
        ]

    def ask_questions(self) -> List[str]:
        import streamlit as st
        answers = []
        st.subheader("Tell us about your dream home:")
        for q in self.questions:
            ans = st.text_area(q, key=q)
            answers.append(ans)
        return answers

    def compile_preferences(self, answers: List[str]) -> str:
        return " ".join(answers).strip()
