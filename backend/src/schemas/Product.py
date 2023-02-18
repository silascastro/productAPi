from pydantic import BaseModel
from typing import Optional, List


from src.schemas.Category import CategorySchema

class ProductBase(BaseModel):
    name: str
    price: float
    serie: int
    image: Optional[str]


class ProductSchema(ProductBase):
    id: Optional[int]
    category_id: Optional[int]

    items: List[CategorySchema] = []

    class Config:
        orm_mode = True