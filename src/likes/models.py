from sqlalchemy import Column, ForeignKey, Integer, Table

from main.db import metadata

likes = Table(
    'likes',
    metadata,
    Column('id', Integer, primary_key=True, index=True,),
    Column('author', ForeignKey('user.id')),
    Column('post', ForeignKey('posts.id')),
)


dislikes = Table(
    'dislikes',
    metadata,
    Column('id', Integer, primary_key=True, index=True,),
    Column('author', ForeignKey('user.id')),
    Column('post', ForeignKey('posts.id')),
)
