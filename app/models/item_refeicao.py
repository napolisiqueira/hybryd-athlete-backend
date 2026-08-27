from pydantic import BaseModel, Field
from typing import Optional

class ItemRefeicao(BaseModel):
    nome: str = Field(description="Nome do alimento")
    quantidade: float = Field(description="Porção do alimento em gramas ou mililitros")
    calorias: float = Field(0 , description="Quantidade total por porção de calorias do alimento")
    proteina: float = Field(0, description="Quantidade total por porção de proteína do alimento")
    carboidrato: float = Field(0, description="Quantidade total por porção de carboidrato do alimento")
    gordura: float = Field(0, description="Quantidade total por porção de gordura do alimento")