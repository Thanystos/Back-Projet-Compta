from fastapi import APIRouter
from fastapi_crudrouter import SQLAlchemyCRUDRouter
from app.database import get_db
from app.models.depense import Depense
from app.schemas.depense import DepenseCreate, DepenseRead

router = APIRouter(
    tags=["Depenses"]
)

crud = SQLAlchemyCRUDRouter(
    schema=DepenseRead,
    create_schema=DepenseCreate,
    db_model=Depense,
    db=get_db
)

router.include_router(crud)
