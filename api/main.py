from fastapi import FastAPI,HTTPException,Depends
from api.database import engine
from api.router import router
from api.models import Base

from pydantic import BaseModel

app=FastAPI()


Base.metadata.create_all(bind=engine)


app.include_router(router, prefix="/books", tags=["Books"])

