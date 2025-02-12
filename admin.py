from fastapi import FastAPI,status
from pydantic import BaseModel
from random import randrange

app=FastAPI()
  
class Post(BaseModel):
    first_name:str
    last_name:str

book=[]

@app.post("/author",status_code=status.HTTP_201_CREATED)
def create_posts(a: Post):
    post_dict = a.dict()
    post_dict['id']= randrange(0,10000)
    book.append(post_dict)
    return {"new_post": post_dict}

 
@app.get("/getposts")
def get_books():
    return {"records":book}

def find_index(id):
    for i,p in enumerate(book):
        if p['id'] == id:
            return i
        
        

@app.delete('/deletepost/{id}',status_code=status.HTTP_204_NO_CONTENT)
def delete_post(id: int):
    index=find_index(id)
    book.pop(index)
    return {"message": "poped "}
