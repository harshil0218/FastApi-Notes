from pydantic import BaseModel
from typing import Optional
from sqlalchemy import Boolean,Integer,Column,ForeignKey,String
from .database import Base

class User(Base):
    __tablename__ = 'users'
    
    id = Column(Integer,primary_key=True,index=True)
    name = Column(String(50))
   
class Blog(Base):
    __tablename__ = 'blogs'
    
    id = Column(Integer,primary_key=True,index=True)
    title = Column(String(50))
    body = Column(String(50))
    published = Column(Boolean)
    user_id = Column(Integer,ForeignKey('users.id'))