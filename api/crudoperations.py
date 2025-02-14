from sqlalchemy.orm import Session
from . import models, schemas

def create_book(db: Session, book: schemas.BookCreate):
    new_book = models.book(title=book.title, author=book.author)
    db.add(new_book)
    db.commit()
    db.refresh(new_book)
    return new_book

def get_books(db: Session):
    return db.query(models.book).all()

def get_book(db: Session, book_id: int):
    return db.query(models.book).filter(models.book.id == book_id).first()

def update_book(db: Session, book_id: int, updated_book: schemas.BookCreate):
    book = db.query(models.book).filter(models.book.id == book_id).first()
    if book:
        book.title = updated_book.title
        book.author = updated_book.author
        db.commit()
        db.refresh(book)
    return book

def delete_book(db: Session, book_id: int):
    book = db.query(models.book).filter(models.book.id == book_id).first()
    if book:
        db.delete(book)
        db.commit()
    return book

