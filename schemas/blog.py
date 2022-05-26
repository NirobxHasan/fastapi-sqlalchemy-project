from turtle import title
from pydantic import BaseModel
from .index import ShowUser

class Blog(BaseModel):
    
    title: str
    body: str
    user_id: int
    
    # class Config:
    #     orm_mode = True


class ShowBlog(BaseModel):
    title: str
    body: str
    creator: ShowUser
    class Config():
        orm_mode = True



