from sqlalchemy import create_engine, Column, Integer, String, Float
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

Base = declarative_base()

class Item(Base):
    __tablename__ = 'items'
    id = Column(Integer, primary_key=True)
    name = Column(String, unique=True)
    price = Column(Float)
    quantity = Column(Integer)

    def __repr__(self):
        return f"<Item(name={self.name}, price={self.price}, quantity={self.quantity})>"

def init_db(uri):
    engine = create_engine(uri)
    Base.metadata.create_all(engine)
    return sessionmaker(bind=engine)
