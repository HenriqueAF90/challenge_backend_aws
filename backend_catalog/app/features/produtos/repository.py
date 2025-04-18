import uuid
from typing import Optional
from boto3.dynamodb.conditions import Key
from app.config import dynamodb_client
from .models import Produto
from .schemas import PostProduto, GetProduto

class ProdutoRepository:
    def __init__(self):
        self.table = dynamodb_client.Table("produtos")

    async def create(self, payload: PostProduto) -> GetProduto:
        produto_id  = str(uuid.uuid4())
        item = payload.model_dump()
        item ["id"] = produto_id
        self.table.put_item(Item=item)
        return(GetProduto(**item))


