from pydantic import BaseModel
from typing import List,Optional

class BookCreate(BaseModel):
    title: str
    author_id :int

class BookResponse(BookCreate):
    book_id:int
    title: str
    
    class Config:
        from_attributes = True



class AuthorCreate(BaseModel):
    author_name: str
    password: str

class AuthorResponse(AuthorCreate):
    author_id: int
    author_name: str

    class Config:
        from_attributes = True

class AuthorLogin(BaseModel):
    author_name:str
    password:str

class Token(BaseModel):
    access_token: str
    token_type: str

class TokenData(BaseModel):
    name: Optional[str]=None
