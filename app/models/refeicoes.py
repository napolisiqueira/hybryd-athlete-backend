from beanie import Document
from pydantic import Field
from typing import Optional
from enum import Enum

from app.models.item_refeicao import ItemRefeicao

class Tipo_refeicao(str, Enum):
    CAFE_DA_MANHA = "café da manhã"
    ALMOCO = "almoço"
    JANTAR = "jantar"
    LANCHE = "lanche"
    PRE_TREINO = "pré-treino"
    INTRA_TREINO = "intra-treino"
    POS_TREINO = "pós-treino"
    OUTRO = "outro"


class Refeicoes(Document):
    nome: str = Field(description="Nome da refeição")
    alimentos: list[ItemRefeicao] = Field([],description="Lista de alimentos que compõem a refeição")
    calorias: float = Field(0, description="Quantidade total de calorias da refeição")
    proteina: float = Field(0 , description="Quantidade total de proteína da refeição")
    carboidrato: float = Field(0, description="Quantidade total de carboidrato da refeição")
    gordura: float = Field(0 , description="Quantidade total de gordura da refeição")
    tipo: Tipo_refeicao = Field(description="Tipo da refeição")


    class Settings:
        name = "refeicoes"

    class Config:
        use_enum_values = True