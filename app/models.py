from sqlalchemy import Column, String, Float, Integer, DateTime
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class PlaneFrame(Base):
    __tablename__ = "plane_frames"

    id = Column(Integer, primary_key=True, autoincrement=True)
    icao = Column(String(4), index=True)
    speed = Column(Float)
    lat = Column(Float)
    lon = Column(Float)
    alt = Column(Integer)
    timestamp = Column(DateTime)
