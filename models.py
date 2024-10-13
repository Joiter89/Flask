import atexit

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, DateTime, Text, func

DSN = 'postgresql://postgres:postgres@localhost:5432/DB'
engine = create_engine(DSN)
atexit.register(engine.dispose)

Session = sessionmaker(bind=engine)
Base = declarative_base(bind=engine)


class Ads(Base):
    __tablename__ = "ads"

    id = Column(Integer, primary_key=True)
    header = Column(String, nullable=False)
    description = Column(Text, nullable=False)
    creation_time = Column(DateTime, server_default=func.now())
    owner = Column(String, nullable=False)


Base.metadata.create_all()