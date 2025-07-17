from fastapi import FastAPI, HTTPException
from sqlalchemy import create_engine, Column, Integer, String, DateTime
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from pydantic import BaseModel
from datetime import datetime

app = FastAPI()

#Database setup (SQLite)
ENGINE = create_engine('sqlite:///launches.db', echo=True)
Base = declarative_base()
class Launch(Base):
    __tablename__= 'launches'
    id = Column(Integer, primary_key=True)
    vehicle = Column(String)
    date = Column(DateTime)
    status = Column(String)

Base.metadata.create_all(ENGINE)
Session = sessionmaker(bind=ENGINE)

class LaunchCreate(BaseModel):
    vehicle: str
    date: datetime
    status: str

class LaunchResponse(LaunchCreate):
    id: int

@app.post("/launches/", response_model=LaunchResponse)
def create_launch(launch: LaunchCreate):
    session = Session()
    db_launch = Launch(vehicle=launch.vehicle, date=launch.date, status=launch.status)
    session.add(db_launch)
    session.commit()
    session.refresh(db_launch)
    return db_launch

@app.get("/launches/{launch_id}", response_model=LaunchResponse)
def get_launch(launch_id: int):
    session = Session()
    db_launch = session.query(Launch).filter(Launch.id == launch_id).first()
    if db_launch is None:
        raise HTTPException(status_code=404, detail="Launch not found")
    return db_launch

@app.get("/launches/")
def get_all_launches():
    session = Session()
    return session.query(Launch).all()