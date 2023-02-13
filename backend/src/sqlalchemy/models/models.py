from sqlalchemy import Column, Integer, String, Double, ForeignKey
from src.sqlalchemy.config.database import Base


class Product(Base):
    __tablename__ = 'product'

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(60))
    category = Column(Integer, ForeignKey("category.id"))
    price = Column(Double)
    serie = Column(Integer)



class Category(Base):
    __tablename__ = 'category'

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(128), nullable=False)