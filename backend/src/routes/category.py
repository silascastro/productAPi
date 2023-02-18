from server import app
from fastapi import Depends, HTTPException
from sqlalchemy.orm import Session
from src.schemas.Category import CategorySchema
from src.infra.sqlalchemy.config.database import create_db, get_db
from src.infra.sqlalchemy.repositories.CategoryRepository import CategoryRepository

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