from fastapi import APIRouter,Depends,HTTPException
from sqlalchemy.orm import Session
from task import schemas
from task.database import get_db
from task.records_handler import author_records
from passlib.context import CryptContext


router=APIRouter()


pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

@router.post("/", response_model=schemas.AuthorResponse)
def create_author(author: schemas.AuthorCreate, db: Session = Depends(get_db)):
    # hashed_password = pwd_context.hash(author.password)  
    # author.password = hashed_password 
    return author_records.create_author(db, author)
        

@router.get("/",response_model=list[schemas.AuthorResponse])
def get_authors(db: Session=Depends(get_db)):
    return author_records.get_authors(db)

@router.get("/{author_id}",response_model=schemas.AuthorResponse)
def get_author(author_id: int,db: Session=Depends(get_db)):
    author=author_records.get_a_author(db,author_id)
    if not author:
        raise HTTPException(status_code=404,detail=f"user not foumd")
    return author

@router.put("/{author_id}", response_model=schemas.AuthorResponse)
def update_author(author_id: int, updated_author: schemas.AuthorCreate, db: Session = Depends(get_db)):
    author = author_records.update_author(db, author_id, updated_author)
    if not author:
        raise HTTPException(status_code=404, detail="Author not found")
    return author


@router.delete("/{author_id}", status_code=204)
def delete_author(author_id: int, db: Session = Depends(get_db)):
    author = author_records.delete_author(db, author_id)
    if not author:
        raise HTTPException(status_code=404, detail="Author not found")
    return {"message": "Author deleted successfully"}






