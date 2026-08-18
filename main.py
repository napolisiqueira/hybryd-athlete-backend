from fastapi import FastAPI
from contextlib import asynccontextmanager
from app.core.database import init_db
from app.routers import health

@asynccontextmanager
async def lifespan(app: FastAPI):
    await init_db()
    yield

app = FastAPI(title="Hybrid Athlete App")

@app.get("/")
def read_root():
    return {"status": "API rodando!"}