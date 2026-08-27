from fastapi import APIRouter, HTTPException
from app.models.exercicios import Alimentos

router = APIRouter(prefix="/Alimentos", tags=["Alimentos"])

@router.post("/", response_model=Alimentos)
async def criar_alimento(alimento: Alimentos):
    await alimento.insert()
    return alimento

@router.get("/{id}", response_model=Alimentos)
async def obter_alimento(id: str):
    alimento = await Alimentos.get(id)
    if not alimento:
        raise HTTPException(status_code=404, detail="Alimento não encontrado")
    return alimento

@router.patch("/{id}", response_model=Alimentos)
async def atualizar_alimento(id: str, alimento: Alimentos):
    alimento_existente = await Alimentos.get(id)
    if not alimento_existente:
        raise HTTPException(status_code=404, detail="Alimento não encontrado")
    await alimento_existente.update(alimento.dict(exclude_unset=True))
    return alimento_existente

@router.delete("/{id}", response_model=Alimentos)
async def deletar_alimento(id: str):
    alimento = await Alimentos.get(id)
    if not alimento:
        raise HTTPException(status_code=404, detail="Alimento não encontrado")
    await alimento.delete()
    return {"status_code": 200, "message": "Alimento deletado com sucesso"}