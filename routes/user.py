import email
from fastapi import APIRouter,Depends, status,Response, HTTPException 
from config.db import get_db
from sqlalchemy.orm import Session
from models  import index
from schemas.index import User,ShowUser
from utils.hasing import Hash


user = APIRouter( prefix="/user",
    tags=["user"],
    responses={404: {"description": "Not found"}},)




@user.post("/")
def create_user(request: User, db: Session = Depends(get_db)):
    new_user = index.User(name= request.name, email=request.email,age=request.age, password=Hash.bcrpt(request.password))
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return new_user

@user.get('/{id}',response_model=ShowUser)
def show_user(id:int, db: Session = Depends(get_db)):
    user = db.query(index.User).filter(index.User.id ==id).first()
    if not user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f'User with the id {id} is not available')
    return user


# @user.get("/")
# async def read_data():
#     return conn.execute(users.select()).fetchall()

# @user.get("/{id}")
# async def read_data_by_id(id: int):
#     return conn.execute(users.select().where(users.c.id ==id)).fetchall()



# @user.post("/")
# async def write_data(user: User):
#     conn.execute(users.insert().values(
#         name = user.name,
#         email = user.email,
#         password = user.password
#     ))
#     return conn.execute(users.select()).fetchall()


# @user.put("/")
# async def update_data(id:int, user:User):
#     conn.execute(users.update().values(
#         name = user.name,
#         email = user.email,
#         password = user.password
#     ).where(users.c.id == id))
#     return conn.execute(users.select()).fetchall()

# @user.delete("/{id}")
# async def detete_data(id:int):
#     conn.execute(users.delete().where(users.c.id == id))
#     return conn.execute(users.select()).fetchall()