import email
from pydantic import BaseModel
from typing import List


class BlogBase(BaseModel):
    
    title: str
    body: str

class Blog(BlogBase):
    class Config():
        orm_mode = True



   

class User(BaseModel):
    name: str
    email: str
    age: int
    password: str


class ShowUser(BaseModel):
    name: str
    email: str
    blogs: List[Blog] = []
    class Config():
        orm_mode = True


