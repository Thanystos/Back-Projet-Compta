from fastapi import FastAPI
from app.routers import health, depense

app = FastAPI()

# Inclusion des routes
app.include_router(health.router)
app.include_router(depense.router)

@app.get("/")
def root():
    return {"message": "Backend opérationnel"}