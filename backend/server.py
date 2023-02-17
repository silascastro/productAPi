from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
from src.schemas.Product import ProductSchema
from src.schemas.Category import CategorySchema
from src.infra.sqlalchemy.config.database import create_db, get_db
from src.infra.sqlalchemy.repositories.ProductRepository import ProductRepository
from src.infra.sqlalchemy.repositories.CategoryRepository import CategoryRepository

create_db()

app = FastAPI()




@app.get('/product')
def getAllProducts(db: Session = Depends(get_db)):
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

@app.delete('/product/{id}')
def deleteProduct(id: int, db: Session = Depends(get_db)):
    return ProductRepository(db).deleteProduct(id=id)



#category route

@app.post('/category')
def createCategory(category: CategorySchema, db: Session = Depends(get_db)):
    newCategory = CategoryRepository(db).createCategory(category)
    return newCategory

@app.get('/category')
def getAllCategories(db: Session = Depends(get_db)):
    return CategoryRepository(db).getAllCategories()

@app.get('/category/{id}')
def getOneCategory(id: int, db: Session = Depends(get_db)):
    db_category = CategoryRepository(db).getOneCategory(id)
    if db_category is None:
        raise HTTPException(status_code=404, detail="category not found")
    return db_category


@app.put('/category/{id}')
def createCategory(id: int, category: CategorySchema, db: Session = Depends(get_db)):
    db_category = CategoryRepository(db).getOneCategory(id)
    if db_category is None:
        raise HTTPException(status_code=404, detail="category not found")
    else:
        return CategoryRepository(db).updateCategory(category=category,id=id)


@app.delete('/category/{id}')
def deleteOneCategory(id: int, db: Session = Depends(get_db)):
    return CategoryRepository(db).deleteCategory(id)
