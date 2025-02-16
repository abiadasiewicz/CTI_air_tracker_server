import datetime
import random
import time

from app.crud import save_frame
from app.database import SessionLocal
from models import PlaneFrame

ICAO_LIST = ["ABCD", "EFGH", "IJKL", "MNOP", "QRST", "UVWX", "YZ12", "3456", "7890", "XYZA"]


def generate_frame(icao):
    return PlaneFrame(
        icao=icao,
        speed=random.uniform(0, 1000),
        lat=random.uniform(-90, 90),
        lon=random.uniform(-180, 180),
        alt=random.randint(0, 10000),
        timestamp=datetime.datetime.now()
    )


def init_generate_frames():
    db = SessionLocal()
    while True:
        for icao in ICAO_LIST:
            frame = generate_frame(icao)
            save_frame(db, frame)
        time.sleep(1)
