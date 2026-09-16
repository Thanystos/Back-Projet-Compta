from sqlalchemy import Column, Integer, String, Float, Date, DateTime
from datetime import datetime
from app.database import Base

class Depense(Base):
    __tablename__ = "depenses"

    id = Column(Integer, primary_key=True, index=True)
    nom = Column(String, nullable=False)
    montant = Column(Float, nullable=False)
    date = Column(Date, nullable=False)
    categorie = Column(String, nullable=True)
    description = Column(String, nullable=True)
    moyen_paiement = Column(String, nullable=True)
    created_at = Column(DateTime, default=datetime.utcnow)
    updated_at = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)
