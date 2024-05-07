from sqlalchemy import create_engine, Column, Integer, String, Float, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, relationship

Base = declarative_base()

class Category(Base):
    __tablename__ = 'categories'
    id = Column(Integer, primary_key=True)
    name = Column(String, unique=True)

    def __repr__(self):
        return f"<Category(id={self.id}, name='{self.name}')>"

class Item(Base):
    __tablename__ = 'items'
    id = Column(Integer, primary_key=True)
    name = Column(String, unique=True)
    price = Column(Float)
    quantity = Column(Integer)
    category_id = Column(Integer, ForeignKey('categories.id'))
    
    # Establish a relationship with the Category model
    category = relationship("Category", back_populates="items")

    def __repr__(self):
        return f"<Item(name={self.name}, price={self.price}, quantity={self.quantity})>"
Category.items = relationship("Item", order_by=Item.id, back_populates="category")

def init_db(uri):
    engine = create_engine(uri)
    Base.metadata.create_all(engine)
    return sessionmaker(bind=engine)
