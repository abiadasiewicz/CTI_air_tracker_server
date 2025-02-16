from fastapi.encoders import jsonable_encoder
from sqlalchemy import text
from sqlalchemy.orm import Session
from app.models import PlaneFrame

def save_frame(db: Session, frame: PlaneFrame):
    db.add(frame)
    db.commit()

def get_latest_frames(db: Session):
    query = text("""
        SELECT DISTINCT ON (icao) * 
        FROM plane_frames 
        ORDER BY icao, timestamp DESC
    """)
    result = db.execute(query)
    columns = result.keys()
    return jsonable_encoder([dict(zip(columns, row)) for row in result.fetchall()])


def get_plane_history(db: Session, icao: str):
    return db.query(PlaneFrame).filter_by(icao=icao).order_by(PlaneFrame.timestamp.asc()).limit(50).all()
