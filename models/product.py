# models/product.py
from sqlalchemy import Column, Integer, String, Float
from config.database import Base

class Product(Base):
    __tablename__ = "products"
    id = Column(Integer, primary_key=True)
    query = Column(String(100))
    title = Column(String(200))
    price = Column(Float)
    link = Column(String(500))
    
class Listing(Base):
    __tablename__ = "listings"
    title = Column(String(200))
    price = Column(String(50))
    location = Column(String(100))
    url = Column(String(500), primary_key=True)  # URL como clave primaria