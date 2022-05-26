from operator import index
from sqlalchemy import Table,Column,Integer,String,ForeignKey
from config.db import Base
from sqlalchemy.orm import relationship


class Blog(Base):
    __tablename__ = 'blogs'
    id = Column(Integer, primary_key=True, index= True)
    title = Column(String(255))
    body = Column(String(255))
    user_id = Column(Integer,ForeignKey('users.id'),nullable=True )
    creator = relationship("User", back_populates ="blogs")
