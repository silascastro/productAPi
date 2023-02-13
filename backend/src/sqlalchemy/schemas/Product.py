from pydantic import BaseModel


class ProductSchema(BaseModel):
    id: int
    name: str
    category: int
    price: float
    serie: int