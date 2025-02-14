from sqlalchemy import Column,Integer,String
from api.database import Base

class book(Base):
    __tablename__= "books"

    id = Column(Integer,primary_key=True,index=True)
    title = Column(String,index=True)
    author = Column(String,index=True)


