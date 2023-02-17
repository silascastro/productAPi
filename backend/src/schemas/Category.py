from pydantic import BaseModel
from typing import Optional, List

from src.schemas.Product import ProductSchema

class CategoryBase(BaseModel):
    name: str


class CategorySchema(CategoryBase):
    id: Optional[int]

    items: List[ProductSchema] = []

    class Config:
        orm_mode = True