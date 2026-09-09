from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.database import get_db
from app.models.depense import Depense
from app.schemas.depense import DepenseCreate, DepenseRead

router = APIRouter(
    prefix="/depenses",
    tags=["depenses"]
)

@router.post("/", response_model=DepenseRead)
def create_depense(depense: DepenseCreate, db: Session = Depends(get_db)):
    db_depense = Depense(nom=depense.nom)
    db.add(db_depense)
    db.commit()
    db.refresh(db_depense)
    return db_depense

@router.get("/", response_model=list[DepenseRead])
def list_depenses(db: Session = Depends(get_db)):
    return db.query(Depense).all()
