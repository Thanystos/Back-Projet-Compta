from fastapi import FastAPI
from app.routers.depense import router as depense_router

app = FastAPI()

app.include_router(depense_router, prefix="/depenses", tags=["Depenses"])
