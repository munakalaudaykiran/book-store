from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from task.records_handler import books_records  # Corrected import name
from task import schemas
from task.database import get_db
from task import oauth2

router = APIRouter()

@router.post("/", response_model=schemas.BookResponse)
def create_book(book: schemas.BookCreate, db: Session = Depends(get_db), author_id: int = Depends(oauth2.get_current_author)):
    print(author_id)
    return books_records.create_book(db, book)

@router.get("/", response_model=list[schemas.BookResponse])
def get_books(db: Session = Depends(get_db),author_id: int = Depends(oauth2.get_current_author)):
    return books_records.get_books(db)

@router.get("/{book_id}", response_model=schemas.BookResponse)
def get_book(book_id: int, db: Session = Depends(get_db),author_id: int = Depends(oauth2.get_current_author)):
    book = books_records.get_book(db, book_id)
    if not book:
        raise HTTPException(status_code=404, detail="Book not found")
    return book

@router.put("/{book_id}", response_model=schemas.BookResponse)
def update_book(book_id: int, updated_book: schemas.BookCreate, db: Session = Depends(get_db),author_id: int = Depends(oauth2.get_current_author)):
    book = books_records.update_book(db, book_id, updated_book)
    if not book:
        raise HTTPException(status_code=404, detail="Book not found")
    return book

@router.delete("/{book_id}", status_code=204)
def delete_book(book_id: int, db: Session = Depends(get_db),author_id: int = Depends(oauth2.get_current_author)):
    book = books_records.delete_book(db, book_id)
    if not book:
        raise HTTPException(status_code=404, detail="Book not found")
    return {"message": "Book deleted successfully"}
