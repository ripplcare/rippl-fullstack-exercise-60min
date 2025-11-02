from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base

engine = create_engine("sqlite:///./app.db", future=True)
SessionLocal = sessionmaker(bind=engine, future=True)
Base = declarative_base()
