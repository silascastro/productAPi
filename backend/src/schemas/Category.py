from pydantic import BaseModel
from typing import Optional, List



class CategoryBase(BaseModel):
    name: str


class CategorySchema(CategoryBase):
    id: Optional[int]



    class Config:
        orm_mode = True