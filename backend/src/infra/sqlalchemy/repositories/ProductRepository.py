from sqlalchemy.orm import Session
from  src.schemas.Product import ProductSchema
from src.infra.sqlalchemy.models import models



class ProductRepository():

    def __init__(self, db: Session):
        self.db = db

    def getProducts(self):
        return self.db.query(models.Product).all()

    def getProductsByCategory(self, category_id: int):
        return self.db.query(models.Product).filter(models.Product.category_id == category_id).all()

    def getOneProduct(self, product_id: int):
        return self.db.query(models.Product).filter(models.Product.id == product_id).first()


    def createProduct(self, product: ProductSchema):
        db_product = models.Product(name = product.name,
            category_id = product.category_id,
            price = product.price,
            serie = product.serie)
        self.db.add(db_product)
        self.db.commit()

        return db_product

    def deleteProduct(self, id: int):
        self.db.query(models.Product).filter(models.Product.id == id).delete()
        self.db.commit()
        return "Product has been deleted"