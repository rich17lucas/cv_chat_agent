# cv_reviewer.py
import os

from openai import OpenAI
from streamlit import secrets


class CVReviewerAgent:
    def __init__(self):
        # Set your OpenAI API key
        api_key = secrets.open_ai.OPENAI_API_KEY
        if not api_key:
            raise ValueError(
                "OpenAI API key not found. Set the OPENAI_API_KEY environment variable."
            )
        self.client = OpenAI(api_key=api_key)

    def review_cv(self, cv_text):
        prompt = (
            "You are an expert career coach. Provide constructive and detailed feedback on the following CV section:\n\n"
            f"{cv_text}\n\n"
            "Feedback:"
        )

        try:
            completion = self.client.chat.completions.create(
                model="gpt-4o-mini",  # Adjust to your preferred model
                messages=[{"role": "user", "content": prompt}],
            )

            feedback = completion.choices[0].message.content
            return feedback
        except Exception as e:
            return f"An error occurred while generating feedback: {e}"

    def is_satisfied(self, feedback):
        prompt = (
            "You are an expert career coach. Based on the following feedback, determine if the CV is satisfactory:\n\n"
            f"{feedback}\n\n"
            "Is the CV satisfactory? (Yes/No):"
        )

        try:
            completion = self.client.chat.completions.create(
                model="gpt-4o-mini",
                messages=[{"role": "user", "content": prompt}],
            )

            satisfaction = completion.choices[0].message.content.strip().lower()
            return satisfaction == "yes"
        except Exception as e:
            return False
