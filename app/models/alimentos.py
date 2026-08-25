from beanie import Document
from pydantic import Field
from typing import Optional
from enum import Enum

class Alimentos(Document):
    nome: Optional[str] = Field(None, description="Nome do alimento")
    calorias: Optional[float] = Field(None, description="Quantidade de calorias em 100g do alimento")
    proteina: Optional[float] = Field(None, description="Quantidade de proteina em 100g do alimento")
    carboidrato: Optional[float] = Field(None, description="Quantidade de carboidrato em 100g do alimento")
    gordura: Optional[float] = Field(None, description="Quantidade de gordura em 100g do alimento")

    class Settings:
        name = "alimentos"

    class Config:
        use_enum_values = True