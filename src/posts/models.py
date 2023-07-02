from datetime import datetime

from sqlalchemy import Column, ForeignKey, Integer, String, Table

from main.db import metadata

posts = Table(
    'posts',
    metadata,
    Column('id', Integer, primary_key=True, index=True,),
    Column('author', ForeignKey('user.id')),
    Column('text', String(1024), nullable=False,),
    Column(
        'created_at',
        String,
        nullable=False,
        default=str(datetime.utcnow().strftime('%Y-%m-%d %H:%M:%S'))
    ),
)
