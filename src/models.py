import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String, Boolean,Text
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine
from eralchemy2 import render_er

Base = declarative_base()

class User(Base):
    __tablename__ = 'user'
    # Here we define columns for the table person
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    name = Column(String(250), nullable=False)
    email = Column(String(80), nullable= False)
    log = Column(Boolean)

class Comments(Base):
    __tablename__ = 'comments'
    id = Column(Integer, primary_key=True)
    coment = Column(String(250))
    user_coment_id = Column(Integer, ForeignKey('user.id'))

class Follow(Base):
    __tablename__ = 'follow'
    id = Column(Integer, primary_key=True)
    id_user_follower = Column(Integer, ForeignKey('user.id'))
    id_user_following = Column(Integer)
    

class LikePost(Base):
    __tablename__ = 'likepost'
    id = Column(Integer, primary_key=True)
    id_user_like = Column(String(250), ForeignKey('user.id'))
    post_id = (Integer, ForeignKey('post.id'))


class Post(Base):
    __tablename__ = 'post'
    id = Column(Integer, primary_key=True)
    img = Column(String(250), nullable=False)
    number_like_post = Column(Integer)
    coments_id = Column(Integer, ForeignKey('comments.id'))

    def to_dict(self):
        return {}

## Draw from SQLAlchemy base
try:
    result = render_er(Base, 'diagram.png')
    print("Success! Check the diagram.png file")
except Exception as e:
    print("There was a problem genering the diagram")
    raise e
