from sqlalchemy import create_engine, Column, Integer, BLOB, String, DateTime
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from datetime import datetime

DATABASE_URL = "mysql+mysqlconnector://root:root@host.docker.internal:3306/database_name"
# DATABASE_URL = "mysql+mysqlconnector://root:root@localhost:3306/database_name"


engine = create_engine(DATABASE_URL)
Base = declarative_base()

class ImagePrediction(Base):    
    __tablename__ = "image_predictions"
    id = Column(Integer, primary_key=True, index=True)
    image_name = Column(BLOB)
    prediction_class = Column(String(length=255))
    created_at = Column(DateTime, default=datetime.utcnow)

Base.metadata.create_all(bind=engine)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

def init_db():
    Base.metadata.create_all(bind=engine)

def save_prediction_to_database(image_data, prediction_class):
    db = SessionLocal()
    db_prediction = ImagePrediction(
        image_name=image_data,
        prediction_class=prediction_class,
    )
    db.add(db_prediction)
    db.commit()
    db.refresh(db_prediction)
    db.close()
