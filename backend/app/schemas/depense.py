from pydantic import BaseModel
from datetime import datetime, date

class DepenseBase(BaseModel):
    nom: str
    montant: float
    date: date
    categorie: str | None = None
    description: str | None = None
    moyen_paiement: str | None = None


class DepenseCreate(DepenseBase):
    pass

class DepenseRead(DepenseBase):
    id: int
    created_at: datetime
    updated_at: datetime

    class Config:
        orm_mode = True
