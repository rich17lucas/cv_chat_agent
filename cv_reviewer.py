# cv_reviewer.py
import os

from dotenv import load_dotenv
from openai import OpenAI

# Load environment variables from .env if you’re using one
load_dotenv(override=True)


class CVReviewerAgent:
    def __init__(self):
        # Set your OpenAI API key
        api_key = os.getenv("OPENAI_API_KEY")
        if not api_key:
            raise ValueError(
                "OpenAI API key not found. Set the OPENAI_API_KEY environment variable."
            )
        self.client = OpenAI(api_key=api_key)

    def review_cv(self, cv_text):
        # Construct the prompt for the OpenAI model
        prompt = (
            "You are an expert career coach. Provide constructive and detailed feedback on the following CV section:\n\n"
            f"{cv_text}\n\n"
            "Feedback:"
        )

        try:
            # Make a request to the OpenAI API
            completion = self.client.chat.completions.create(
                model="gpt-4o-mini",  # Adjust to your preferred model
                messages=[{"role": "user", "content": prompt}],
            )

            feedback = completion.choices[0].message.content.strip()
            return feedback
        except Exception as e:
            return f"An error occurred while generating feedback: {e}"
