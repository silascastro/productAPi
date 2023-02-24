from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

SQLALCHEMY_DATABASE_URL = "mysql+pymysql://qt7i6uqcxseb5rc6:jwm48v2t2io13tjg@tvcpw8tpu4jvgnnq.cbetxkdyhwsb.us-east-1.rds.amazonaws.com:3306/xzq1aq1b6nhcxxfz"
#SQLALCHEMY_DATABASE_URL = "sqlite:///./sql_app.db"
# SQLALCHEMY_DATABASE_URL = "postgresql://user:password@postgresserver/db"


# engine = create_engine(
#     SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread": False}
# )

engine = create_engine(
    SQLALCHEMY_DATABASE_URL
)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()

def create_db():
    Base.metadata.create_all(bind=engine)

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()