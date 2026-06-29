from dotenv import load_dotenv
import os

load_dotenv()


class Settings:
    app_name = "ResearchMind AI"

    app_version = "1.0.0"

    api_prefix = "/api/v1"

    gemini_api_key = os.getenv("GEMINI_API_KEY")


settings = Settings()