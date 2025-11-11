from fastapi import FastAPI
from app.db.connections import db, engine
from app.models.base import Base
from app.api.item_resource import api_router 

app = FastAPI()
app.include_router(api_router)

@app.get("/")
def health():
    return {"ok": "200"}

