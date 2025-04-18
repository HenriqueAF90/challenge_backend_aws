from pydantic import BaseModel, Field, condecimal
from typing import Optional

class PostProduto(BaseModel):
    nome: str = Field(..., example="Tênis esportivo")
    descricao: Optional[str] = Field(None, example="Tênis esportivo de couro")
    preco: str = Field(..., example="99.90")
    id_categoria: str = Field(..., example="categoria-xpto")
    owner_id: str = Field(..., example="owner-xpto")

class GetProduto(PostProduto):
    id: str = Field(..., example="produto-xpto")
