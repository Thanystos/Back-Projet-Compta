from sqlalchemy import Column, Integer, String
from app.database import Base

class Depense(Base):
    __tablename__ = "depenses"

    id = Column(Integer, primary_key=True, index=True)
    nom = Column(String, nullable=False)
