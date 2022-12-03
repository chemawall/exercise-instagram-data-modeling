import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String, Bolean
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
    activity_id = Column(Integer)
    email = Column(String(80), nullable= False)
    log = Column(Bolean)
    followers_id = Column(Integer)
    followings_id = Column(Integer)

class Activity(Base):
    __tablename__ = 'activity'
    # Here we define columns for the table person
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    coments_id = Column(Integer)
    like_post_id = Column(Integer)
    like_coments_id = Column(Integer)
    post_id = Column(Integer)

class Followings(Base):
    __tablename__ = 'followings'
    # Here we define columns for the table person
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    name = Column(String(250), nullable=False)

class Followers(Base):
    __tablename__ = 'followers'
    # Here we define columns for the table person
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    name = Column(String(250), nullable=False)

class LikePost(Base):
    __tablename__ = 'likepost'
    # Here we define columns for the table person
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    name = Column(String(250), nullable=False)
    post_id = (Integer)

class LikeComent(Base):
    __tablename__ = 'like_post'
    # Here we define columns for the table person
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    like_coment = Column(Bolean)
    post_id = (Integer)

class Post(Base):
    __tablename__ = 'post'
    # Here we define columns for the table address.
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    img = Column(String(250), nullable=False)
    text = Column(text)
    number_like_post = Column(Integer)
    coments_id = Column(Integer)
    person_id = Column(Integer, ForeignKey('person.id'))
    person = relationship(Person)

    def to_dict(self):
        return {}

## Draw from SQLAlchemy base
try:
    result = render_er(Base, 'diagram.png')
    print("Success! Check the diagram.png file")
except Exception as e:
    print("There was a problem genering the diagram")
    raise e
