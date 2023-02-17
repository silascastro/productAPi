from sqlalchemy import Column, Integer, String, Double, ForeignKey
from src.infra.sqlalchemy.config.database import Base
from sqlalchemy.orm import relationship


class Product(Base):
    __tablename__ = 'product'

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    name = Column(String(60))
    category_id = Column(Integer, ForeignKey("category.id"))
    price = Column(Double)
    serie = Column(Integer)

    categories = relationship("Category", back_populates="product_list")



class Category(Base):
    __tablename__ = 'category'

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    name = Column(String(128), nullable=False)

    product_list = relationship("Product", back_populates="categories")