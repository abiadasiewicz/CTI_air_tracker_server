from fastapi import FastAPI, Depends
from sqlalchemy.orm import Session
from app.database import SessionLocal
from app.crud import get_latest_frames, get_plane_history

app = FastAPI()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.get("/planes")
def read_latest_planes(db: Session = Depends(get_db)):
    return get_latest_frames(db)

@app.get("/planeHistory")
def read_plane_history(icao: str, db: Session = Depends(get_db)):
    return get_plane_history(db, icao)