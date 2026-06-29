import google.generativeai as genai

from app.core.config import settings


class GeminiService:

    def __init__(self):

        genai.configure(api_key=settings.gemini_api_key)

        self.model = genai.GenerativeModel("gemini-2.5-flash")

    def generate_answer(self, prompt: str):

        response = self.model.generate_content(prompt)

        return response.text