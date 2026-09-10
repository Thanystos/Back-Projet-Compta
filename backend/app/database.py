from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base
import os

DATABASE_URL = os.getenv("DATABASE_URL")

# Engine SQLAlchemy
engine = create_engine(
    DATABASE_URL,
    echo=False,  # mets True si tu veux voir les requêtes SQL
)

# Session locale
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Base pour les modèles ORM
Base = declarative_base()


# Dépendance FastAPI pour obtenir une session DB
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# IMPORTANT : importer les modèles APRÈS la définition de Base
from app import models