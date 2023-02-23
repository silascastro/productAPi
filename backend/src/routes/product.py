from server import app
from fastapi import Depends, HTTPException
from sqlalchemy.orm import Session
from src.schemas.Product import ProductSchema
from src.schemas.Category import CategorySchema
from src.infra.sqlalchemy.models import models
from src.infra.sqlalchemy.config.database import get_db
from src.infra.sqlalchemy.repositories.ProductRepository import ProductRepository
from src.infra.sqlalchemy.repositories.CategoryRepository import CategoryRepository


@app.get('/product')
def getAllProducts( db: Session = Depends(get_db)):
    createBasicCategories(db)
    return ProductRepository(db).getProducts()

@app.get('/product/{id}')
def getAllProducts(id: int, db: Session = Depends(get_db)):
    return ProductRepository(db).getOneProduct(id)

@app.get('/product/category/{id}')
def getAllProducts(id: int, db: Session = Depends(get_db)):
    return ProductRepository(db).getProductsByCategory(id)

@app.post('/product')
def createProduct(product: ProductSchema, db: Session = Depends(get_db)):
    newproduct = ProductRepository(db).createProduct(product)
    return newproduct

@app.put('/product/{id}')
def createProduct(id: int, product: ProductSchema, db: Session = Depends(get_db)):
    db_product = ProductRepository(db).getOneProduct(id)
    if db_product is None:
        raise HTTPException(status_code=404, detail="category not found")
    else:
        if product.image is None:
            return ProductRepository(db).updateProductWithoutImage(id=id, product=product)
        else:
            return ProductRepository(db).updateProductWithImage(id=id, product=product)


@app.delete('/product/{id}')
def deleteProduct(id: int, db: Session = Depends(get_db)):
    return ProductRepository(db).deleteProduct(id=id)

def createBasicCategories(db):
    categories = [CategorySchema(name="Smartphones"), CategorySchema(name="Appliances"), CategorySchema(name="Tv & Audio")]
    allCategoriesCreated = CategoryRepository(db).getAllCategories()

    if(len(allCategoriesCreated) == 0):
        for category in categories:
            CategoryRepository(db).createCategory(category)