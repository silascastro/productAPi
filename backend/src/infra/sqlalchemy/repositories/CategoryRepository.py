from sqlalchemy.orm import Session
from  src.schemas.Category import CategorySchema
from src.infra.sqlalchemy.models import models



class CategoryRepository():

    def __init__(self, db: Session):
        self.db = db

    def getAllCategories(self):
        return self.db.query(models.Category).all()

    def getOneCategory(self, category_id: int):
        return self.db.query(models.Category).filter(models.Category.id == category_id).first()


    def createCategory(self, category: CategorySchema):
        db_category = models.Category(name = category.name)
        self.db.add(db_category)
        self.db.commit()
        return db_category

    def updateCategory(self, id:int, category: CategorySchema):
        self.db.query(models.Category).filter(models.Category.id == id).update({models.Category.name : category.name})
        self.db.commit()
        return "Category has been updated"


    def deleteCategory(self, id: int):
        self.db.query(models.Category).filter(models.Category.id == id).delete()
        self.db.commit()
        return "Category has been deleted"