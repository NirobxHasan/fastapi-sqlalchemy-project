from turtle import title
from fastapi import APIRouter, Depends, status,Response, HTTPException 
from sqlalchemy.orm import Session
from config.db import get_db
from  schemas.index import Blog, ShowBlog
from models  import index
from typing import List
blogRoute = APIRouter(
    prefix="/blog",
    tags=["blog"],
    responses={404: {"description": "Not found"}},
)





@blogRoute.post('/', status_code=status.HTTP_201_CREATED)
def create(request:Blog, db: Session = Depends(get_db) ):
    new_blog = index.Blog(title= request.title, body= request.body, user_id= request.user_id)
    db.add(new_blog)
    db.commit()
    db.refresh(new_blog)
    return new_blog


@blogRoute.get('/', response_model=List[ShowBlog])
def all(db: Session = Depends(get_db)):
    blogs = db.query(index.Blog).all()
    return blogs

@blogRoute.put('/{id}', status_code=status.HTTP_202_ACCEPTED)
def update(id,request:Blog,  db: Session = Depends(get_db)):
   
    blog = db.query(index.Blog).filter(index.Blog.id == id)
    print(blog)
    if not blog.first():
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail=f'Blog with the id {id} is not available')
    blog.update({'title': request.title, 'body':request.body})
    db.commit()
    return 'update'


@blogRoute.get('/{id}', response_model=ShowBlog)
def show(id: int, response:Response, db: Session = Depends(get_db)):
    blog= db.query(index.Blog).filter(index.Blog.id == id).first()
    if not blog:
        # response.status_code = status.HTTP_404_NOT_FOUND
        # return {'detail': f"Blog with the id {id} is not available"}
        # Alternative
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f'Blog with the id {id} is not available') 
    return blog


@blogRoute.delete('/{id}',status_code=status.HTTP_204_NO_CONTENT)
def distroy(id:int, db: Session = Depends(get_db),  ):
    db.query(index.Blog).filter(index.Blog.id == id).delete(synchronize_session=False)
    
    db.commit()
    return 'done'