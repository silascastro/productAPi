from sqlalchemy.orm import Session
from  src.schemas.Review import ReviewSchema
from src.infra.sqlalchemy.models import models



class ReviewRepository():

    def __init__(self, db: Session):
        self.db = db

    def getAllReviewsFromProduct(self, product_id: int):
        return self.db.query(models.Review).filter(models.Review.product_id == product_id).all()

    def createReview(self, review: ReviewSchema):
        db_review = models.Review(title=review.title, comentary=review.comentary, rate=review.rate, product_id=review.product_id)
        self.db.add(db_review)
        self.db.commit()
        return db_review


