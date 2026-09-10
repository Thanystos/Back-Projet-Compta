from pydantic import BaseSettings

class Settings(BaseSettings):
    app_name: str = "Projet Compta"
    database_url: str = "sqlite:///./app.db"

settings = Settings()
