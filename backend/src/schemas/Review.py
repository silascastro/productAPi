from pydantic import BaseModel
from typing import Optional


class ReviewSchema(BaseModel):
    id: Optional[int]
    title: Optional[str]
    comentary: Optional[str]
    rate: Optional[int]
    product_id: Optional[int]
