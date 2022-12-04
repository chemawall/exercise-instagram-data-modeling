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
    activity_id = Column(Integer, ForeignKey('activity.id'))
    email = Column(String(80), nullable= False)
    log = Column(Boolean)
    followers_id = Column(Integer, ForeignKey('followers.id'))
    followings_id = Column(Integer, ForeignKey('followings.id'))

class Activity(Base):
    __tablename__ = 'activity'
    id = Column(Integer, primary_key=True)
    coments_id = Column(Integer, ForeignKey('coments.id'))
    like_post_id = Column(Integer, ForeignKey('likepost.id'))
    like_coments_id = Column(Integer, ForeignKey('likecoment.id'))
    post_id = Column(Integer,ForeignKey('post.id'))

class Followings(Base):
    __tablename__ = 'followings'
    id = Column(Integer, primary_key=True)
    name = Column(String(80), nullable=False)

class Followers(Base):
    __tablename__ = 'followers'
    id = Column(Integer, primary_key=True)
    name = Column(String(80), nullable=False)

class LikePost(Base):
    __tablename__ = 'likepost'
    id = Column(Integer, primary_key=True)
    name = Column(String(250), nullable=False)
    post_id = (Integer, ForeignKey('post.id'))

class LikeComent(Base):
    __tablename__ = 'likecoment'
    id = Column(Integer, primary_key=True)
    like_coment = Column(Boolean)
    post_id = (Integer,ForeignKey('post.id'))

class Post(Base):
    __tablename__ = 'post'
    id = Column(Integer, primary_key=True)
    img = Column(String(250), nullable=False)
    text = Column(Text)
    number_like_post = Column(Integer)
    coments_id = Column(Integer, ForeignKey('coments.id'))

    def to_dict(self):
        return {}

## Draw from SQLAlchemy base
try:
    result = render_er(Base, 'diagram.png')
    print("Success! Check the diagram.png file")
except Exception as e:
    print("There was a problem genering the diagram")
    raise e
