from fastapi import FastAPI,status
from fastapi.params import Body
from pydantic import BaseModel
from random import randrange

app=FastAPI()

class Post(BaseModel):
    title:str
    context:str
    publish:bool = True

# class course(BaseModel):
#     name:str
#     fee:int
#     duration:str

# @app.post("/courses",status_code=status.HTTP_201_CREATED)
# def c_posts(c1:course):
#     '''
#     # this is the endpoint
#     this is the endpoint
#     '''
#     my_posts.append(c1)
#     print(c1.fee)
#     return {"course details" :f"name {c1.name} fee {c1.fee}"}

my_posts=[]
@app.get("/")
def root():
    return {"message":my_posts}

@app.post("/createposts")
def create_posts(post: Post):
    post_dict = post.dict()
    post_dict['id']= randrange(0,10000)
    my_posts.append(post_dict)
    return {"new_post": post_dict}

# def find_post(id):
#     for p in my_posts:
#         if p['id'] == id:
#             return p
        
# def find_index_post(id):
#     for i, p in enumerate (my_posts):
#         if p['id']==id:
#             return i
        
# @app.delete("posts/{id}")
# def delete_post(id: int):
#     index=find_index_post(id)
#     my_posts.pop(index)
#     return {"message":"deleted succesfully"}

# @app.get("/post/{id}")
# def get_post(id: int):
#     post = find_post(id)
#     print(post)
#     return {"post_detail" : post}

