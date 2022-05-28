from fastapi import APIRouter, Depends,HTTPException,status
from sqlalchemy.orm import Session
from config.db import get_db
from schemas.index import Login
from models.index import User
from utils.hasing import Hash
from utils.JWTtoken import create_access_token
from datetime import timedelta
from fastapi.security import OAuth2PasswordRequestForm
loginRouter = APIRouter( 
    prefix="/login",
    tags=["authentication"]
    )


@loginRouter.post("/")
def login(request:OAuth2PasswordRequestForm=Depends(), db: Session = Depends(get_db)):
    user = db.query(User).filter(User.email == request.username).first()
    if not user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail=f'invalid credantial')
    if not Hash.verify(user.password , request.password):
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail=f'invalid password')
    ACCESS_TOKEN_EXPIRE_MINUTES = 30
    access_token_expires = timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    access_token = create_access_token(
        data={"sub": user.email}, expires_delta=access_token_expires
    )
    return {"access_token": access_token, "token_type": "bearer"}