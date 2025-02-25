from sqlalchemy.orm import Session,joinedload
from task import models, schemas
from task.utils import hashpassword

def create_author(db: Session, author: schemas.AuthorCreate):
    hashed_password = hashpassword(author.password)
    new_author=models.Author_details(author_name=author.author_name,password=hashed_password)
    db.add(new_author)
    db.commit()
    db.refresh(new_author)
    return new_author

def get_authors(db: Session):
    return db.query(models.Author_details).all()

def get_a_author(db:Session,author_id:int):
    return db.query(models.Author_details).options(joinedload(models.Author_details.books)).filter(models.Author_details.author_id == author_id).first()

def update_author(db: Session, author_id: int, updated_author: schemas.AuthorCreate):
    author = db.query(models.Author_details).filter(models.Author_details.author_id == author_id).first()
    if author:
        author.author_name = updated_author.author_name
        db.commit()
        db.refresh(author)
        return author
    return None

def delete_author(db: Session, author_id: int):
    author = db.query(models.Author_details).filter(models.Author_details.author_id == author_id).first()
    if author:
        db.delete(author)
        db.commit()
        return author
    return None
