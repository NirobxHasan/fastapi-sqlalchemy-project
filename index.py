from fastapi import FastAPI
from routes.index import user,blogRoute,loginRouter
from models import index
from config.db import engine,Base

app = FastAPI()
Base.metadata.create_all(engine)
# @app.get("/")
# def read_something():
#     return {"msg": "Hello Word"}


app.include_router(user)
app.include_router(blogRoute)
app.include_router(loginRouter)


 
