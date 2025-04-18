from fastapi import APIRouter, HTTPException, status
from typing import List
from .schemas import PostProduto, GetProduto
from .repository import ProdutoRepository
from .service import ProdutoService  
router = APIRouter()  

router = APIRouter(prefix="/productos", tags=["Productos"])


repository = ProdutoRepository()
service  = ProdutoService(repository)

@router.post("/", response_model=GetProduto, status_code=status.HTTP_201_CREATED)
async def create_produto(produto: PostProduto):
    return await service.create_produto(produto)



