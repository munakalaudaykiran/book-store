from sqlalchemy.orm import Session
from task import models, schemas

def create_book(db: Session, book: schemas.BookCreate):
    new_book = models.Books_details(title=book.title, author_id=book.author_id)
    db.add(new_book)
    db.commit()
    db.refresh(new_book)
    return new_book

def get_books(db: Session):
    return db.query(models.Books_details).all()

def get_book(db: Session, book_id: int):
    return db.query(models.Books_details).filter(models.Books_details.book_id == book_id).first()


def update_book(db: Session, book_id: int, updated_book: schemas.BookCreate):
    book = db.query(models.Books_details).filter(models.Books_details.book_id== book_id).first()
    if book:
        book.title = updated_book.title
        book.author_id = updated_book.author_id
        db.commit()
        db.refresh(book)
        return book
    return None
def delete_book(db: Session, book_id: int):
    book = db.query(models.Books_details).filter(models.Books_details.book_id == book_id).first()
    if book:
        db.delete(book)
        db.commit()
        return book
    return None




