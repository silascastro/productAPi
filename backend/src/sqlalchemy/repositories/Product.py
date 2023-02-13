from sqlalchemy.orm import Session
from  src.sqlalchemy.schemas.Product import ProductSchema
from src.sqlalchemy.models import models



class ProductRepository:

    def __init__(self, db: Session):
        self.db = db

    def getProducts( user_id: int):
        return db.query(models.User).filter(models.User.id == user_id).first()

    def getOneProduct( user_id: int):
        return db.query(models.User).filter(models.User.id == user_id).first()


    def createProduct( user_id: int, product: ProductSchema):
        db_product = models.Product(nome = product.name,
         category = product.category,
          price = product.price,
          serie = product.serie)
        return db.query(models.User).filter(models.User.id == user_id).first()