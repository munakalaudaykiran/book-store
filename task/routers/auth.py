from fastapi import APIRouter,HTTPException,Depends
from sqlalchemy.orm import Session
from task import schemas,models,utils,oauth2
from task.database import get_db
import logging

router = APIRouter()

@router.post("/login")
def login(author_credentials:schemas.AuthorLogin,db:Session=Depends(get_db)):
    author=db.query(models.Author_details).filter(models.Author_details.author_name == author_credentials.author_name).first()
    print("🔹 Author Instance:", author.__dict__)

    logging.debug(f"🔹 Author Instance: {author.__dict__}")

    print("Author Data Being Sent to Token:", {
        "author_name": author.author_name,
        "author_id": author.author_id
    })
    # if not author: 
    #     raise HTTPException(status_code=401,detail=f"invalid cerdentials")
    if not author or utils.verify_password(author_credentials.password,author.password):
        raise HTTPException(status_code=403,detail=f"invalid credentials")
    
    access_token = oauth2.create_access_token(data = {"author_name": author.author_name,"author_id": author.author_id})
    return {"token": access_token,"token_key":"bearer"}