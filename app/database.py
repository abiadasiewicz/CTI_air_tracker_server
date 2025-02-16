from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

DATABASE_URL = "postgresql://user:password@db:5432/CTI_db"

engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(bind=engine)
