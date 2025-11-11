from sqlalchemy import Column, DateTime, DateTime, Integer, String
from app.models.base import Base, CustomBase


class Item(CustomBase):
    __tablename__ = "items"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True, unique=True)
    description = Column(String)
    price = Column(Integer, nullable=False)
    
