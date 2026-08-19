from fastapi import FastAPI
from contextlib import asynccontextmanager
from app.core.database import init_db
from app.routers import exercicio, health


@asynccontextmanager
async def lifespan(app: FastAPI):
    await init_db()
    yield

app = FastAPI(lifespan=lifespan, title="Hybrid Athlete App")
app.include_router(health.router)
app.include_router(exercicio.router)

@app.get("/")
def read_root():
    return {"status": "API rodando!"}