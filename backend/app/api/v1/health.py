from fastapi import APIRouter
from app.schemas.health import HealthStatus

router = APIRouter(
    prefix="/health",
    tags=["health"]
)

@router.get("/", response_model=HealthStatus)
def health_check():
    return HealthStatus(status="Route health intégralement config")
