from dataclasses import dataclass
from typing import Optional


@dataclass
class Produto:
    id: str
    title: str
    description: Optional[str]
    price: str
    category_id: str
    owner_id: str
