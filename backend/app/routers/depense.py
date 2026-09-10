from fastapi_crudrouter import SQLAlchemyCRUDRouter
from app.database import get_db
from app.models.depense import Depense
from app.schemas.depense import DepenseCreate, DepenseRead

router = SQLAlchemyCRUDRouter(
    schema=DepenseRead,
    create_schema=DepenseCreate,
    db_model=Depense,
    db=get_db
)
