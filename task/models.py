from sqlalchemy import Column,Integer,String,DateTime,ForeignKey
from sqlalchemy.sql import func
from sqlalchemy.orm import relationship
from task.database import Base

class Author_details(Base):
    __tablename__ = "author"
    author_id = Column(Integer,primary_key=True,nullable=False,index=True)
    author_name= Column(String,nullable=False)
    password=Column(String,nullable=False)
    books = relationship("Books_details", back_populates="author")
    

class Books_details(Base):
    __tablename__ = "books"
    book_id = Column(Integer,primary_key=True,index=True)
    title= Column(String,nullable=False)
    created_at= Column(DateTime, default=func.now())
    author_id = Column(Integer,ForeignKey("author.author_id"),index=True)
    author = relationship("Author_details", back_populates="books")


