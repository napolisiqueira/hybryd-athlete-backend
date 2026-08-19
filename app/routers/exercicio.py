from fastapi import APIRouter, HTTPException
from app.models.exercicios import Exercicio

router = APIRouter(prefix="/exercicios", tags=["Exercicios"])

@router.post("/", response_model=Exercicio)
async def criar_exercicio(exercicio: Exercicio):
    await exercicio.insert()
    return exercicio

@router.get("/", response_model=list[Exercicio])
async def listar_exercicios():
    return await Exercicio.find_all().to_list()

@router.get("/{exercicio_id}", response_model=Exercicio)
async def obter_exercicio(exercicio_id: str):
    exercicio = await Exercicio.get(exercicio_id)
    if not exercicio:
        raise HTTPException(status_code=404, detail="Exercício não encontrado")
    return exercicio

@router.delete("/{exercicio_id}", response_model=Exercicio)
async def deletar_exercicio(exercicio_id: str):
    exercicio = await Exercicio.get(exercicio_id)
    if not exercicio:
        raise HTTPException(status_code=404, detail="Exercício não encontrado")
    await exercicio.delete()
    return {"status_code": 200, "message": "Exercício deletado com sucesso"}

@router .patch("/{exercicio_id}", response_model=Exercicio)
async def atualizar_exercicio(exercicio_id: str, exercicio_atualizado: Exercicio):
    exercicio = await Exercicio.get(exercicio_id)
    if not exercicio:
        raise HTTPException(status_code=404, detail="Exercício não encontrado")
    await exercicio.update({"$set": exercicio_atualizado.model_dump(exclude_unset=True)})
    return exercicio
