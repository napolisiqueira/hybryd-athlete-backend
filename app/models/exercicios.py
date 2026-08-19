from beanie import Document
from pydantic import Field
from typing import Optional
from enum import Enum

class GrupoMusucular(str, Enum):
    PEITO = "peito"
    COSTAS = "costas"
    OMBROS = "ombros"
    BICEPS = "biceps"
    TRICEPS = "triceps"
    GLUTEOS = "gluteos"
    ABDOMINAL = "abdomem"
    PERNAS = "pernas"
    PANTURRILHA = "panturrilha"
    CARDIO = "cardio"

class Equipamento(str, Enum):
    HALTERES = "halteres"
    BARRA = "barra"
    MAQUINA = "maquina"
    CABO = "cabo"
    ELASTICO = "elastico"
    PESO_CORPORAL = "peso_corporal"
    KETTLEBELL = "kettlebell"
    OUTRO = "outro"


class Exercicio(Document):
    nome: Optional[str] = Field(None, description="Nome do exercício")
    grupo_muscular: Optional[GrupoMusucular] = Field(None, description="Grupo muscular alvo do exercício")
    equipamento: Optional[Equipamento] = Field(None, description="Equipamento necessário para o exercício")
    descricao: Optional[str] = Field(None, description="Descrição detalhada do exercício")
    imagem_url: Optional[str] = Field(None, description="URL da imagem do exercício")

    class Settings:
        name = "exercicios"

    class Config:
        use_enum_values = True
