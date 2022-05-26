import email
from operator import index
from tokenize import String
from sqlalchemy import Table,Column,Integer,String
from config.db import Base
from sqlalchemy.orm import relationship
# from .blog import Blog


class User(Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key= True, index= True)
    name =Column(String(255))
    email =Column(String(255))
    password = Column(String(255))
    blogs = relationship("Blog", back_populates ="creator")
