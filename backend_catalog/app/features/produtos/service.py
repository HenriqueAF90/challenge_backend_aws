from typing import Optional
from .schemas import PostProduto, GetProduto
from .repository import ProdutoRepository

class ProdutoService:
    def __init__(self, repository: ProdutoRepository):
        self.repository = repository

    async def create_produto(self, payload: PostProduto) -> GetProduto:
        return await self.repository.create(payload)
