from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    app_name: str = "ResearchMind AI"
    app_version: str = "1.0.0"
    debug: bool = True
    host: str = "127.0.0.1"
    port: int = 8000
    api_prefix: str = "/api/v1"

    class Config:
        env_file = ".env"


settings = Settings()