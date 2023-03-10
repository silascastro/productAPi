from main import app
from fastapi import Depends, HTTPException
from sqlalchemy.orm import Session
from src.schemas.Review import ReviewSchema
from src.infra.sqlalchemy.config.database import get_db
from src.infra.sqlalchemy.repositories.ReviewRepository import ReviewRepository


@app.get('/review/{id}')
def getAllReviewsFromProduct(id: int, db: Session = Depends(get_db)):
    return ReviewRepository(db).getAllReviewsFromProduct(product_id=id)

@app.post('/review')
def createProduct(review: ReviewSchema, db: Session = Depends(get_db)):
    newReview = ReviewRepository(db).createReview(review=review)
    return newReview

