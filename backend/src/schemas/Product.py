from pydantic import BaseModel
from typing import Optional


class ProductBase(BaseModel):
    name: str
    price: float
    serie: int


class ProductSchema(ProductBase):
    id: Optional[int]
    category_id: int

    class Config:
        orm_mode = True