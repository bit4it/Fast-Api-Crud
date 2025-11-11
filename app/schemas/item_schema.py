from datetime import datetime
from pydantic import BaseModel, ConfigDict
from typing import Union

class ItemSchema(BaseModel):
    name: str
    description: str
    price: int
    created_at: datetime = None
    updated_at: datetime = None  
    model_config = ConfigDict(from_attributes=True)


# id = Column(Integer, primary_key=True, index=True)
#     name = Column(String, index=True)
#     description = Column(String)
#     price = Column(Integer)

#     created_at = Column(DateTime, default=datetime.utcnow)
#     updated_at = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)
