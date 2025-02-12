from fastapi import APIRouter, status, HTTPException
from random import randrange
from app.models import Post
from app.database import book
from app.utils import find_index

router = APIRouter()

@router.post("/author", status_code=status.HTTP_201_CREATED)
def create_posts(a:Post):
    post_dict = a.model_dump()
    post_dict['id'] = randrange(0, 10000)
    book.append(post_dict)
    return {"new_post": post_dict}

@router.get("/getposts")
def get_books():
    return {"records": book}

@router.delete("/deletepost/{id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_post(id: int):
    index = find_index(id)

    if index is None:  
        raise HTTPException(status_code=404, detail="Post not found")

    del book[index] 
    return {"message": "Post deleted successfully"}
