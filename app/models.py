from pydantic import BaseModel

class Post(BaseModel):
    first_name: str
    last_name: str
