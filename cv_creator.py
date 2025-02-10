# cv_creator.py
import os

import openai
from dotenv import load_dotenv
from openai import OpenAI
from streamlit import secrets

# Load environment variables from .env if you’re using one
load_dotenv(override=True)


class CVCreatorAgent:
    def __init__(self):
        # Set your OpenAI API key
        # api_key = os.getenv("OPENAI_API_KEY")
        api_key = secrets.open_ai.OPENAI_API_KEY
        if not api_key:
            raise ValueError(
                "OpenAI API key not found. Set the OPENAI_API_KEY environment variable."
            )
        self.client = OpenAI(api_key=api_key)

    def create_cv_section(self, prompt):
        # Construct the prompt for the OpenAI model
        full_prompt = (
            "You are an expert CV writer. Generate a well-structured and professional CV section based on the following prompt:\n\n"
            f"{prompt}\n\n"
            "CV Section:"
        )

        try:
            # Make a request to the OpenAI API
            completion = self.client.chat.completions.create(
                model="gpt-4o-mini",  # Choose a suitable model
                messages=[{"role": "user", "content": full_prompt}],
            )

            # cv_section = response.choices[0].text.strip()
            cv_section = completion.choices[0].message.content
            return cv_section
        except Exception as e:
            return f"An error occurred while generating the CV section: {e}"
