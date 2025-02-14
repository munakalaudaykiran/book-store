from pydantic import BaseModel

class BookCreate(BaseModel):
    title: str
    author: str

class BookResponse(BookCreate):
    id: int

    class Config:
        from_attributes = True
