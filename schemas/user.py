import email
from pydantic import BaseModel
from typing import List
# from .blog import Blog
   

class User(BaseModel):
    name: str
    email: str
    password: str


class ShowUser(BaseModel):
    name: str
    email: str
    # blogs: List[B] = []
    class Config():
        orm_mode = True


