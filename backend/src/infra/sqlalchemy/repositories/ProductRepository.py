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
            image = product.image,
            price = product.price,
            serie = product.serie)
        self.db.add(db_product)
        self.db.commit()

        return db_product

    def updateProductWithImage(self, id:int, product: ProductSchema):
        self.db.query(models.Product).filter(models.Product.id == id).update({models.Product.name : product.name,
                                                                              models.Product.image: product.image,
                                                                              models.Product.price: product.price, models.Product.serie: product.serie})
        self.db.commit()
        return "Product has been updated"

    def updateProductWithoutImage(self, id:int, product: ProductSchema):
        self.db.query(models.Product).filter(models.Product.id == id).update({models.Product.name : product.name,
                                                                              models.Product.price: product.price, models.Product.serie: product.serie})
        self.db.commit()
        return "Product has been updated"

    def deleteProduct(self, id: int):
        self.db.query(models.Review).filter(models.Review.product_id == id).delete();
        self.db.query(models.Product).filter(models.Product.id == id).delete()
        self.db.commit()
        return "Product has been deleted"