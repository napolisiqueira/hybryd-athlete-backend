from fastapi import APIRouter, HTTPException
from app.models.exercicios import Alimentos

router = APIRouter(prefix="/Alimentos", tags=["Alimentos"])

@router.post("/", response_model=Alimentos)
async def criar_alimento(alimento: Alimentos):
    await alimento.insert()
    return alimento