from fastapi import APIRouter
from app.api.v1 import depense
from app.api.v1.health import router as health_router
from app.api.v1.depense import router as depense_router


api_router = APIRouter()

api_router.include_router(health_router, prefix="/api/v1")
api_router.include_router(depense_router, prefix="/api/v1")