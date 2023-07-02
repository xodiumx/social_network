from fastapi import FastAPI

from likes.router import router as likes_router
from posts.router import router as posts_router
from users.router import router as users_router

tags_metadata = [
    {
        'name': 'auth',
        'description': 'Authentication and authorization'
    },
    {
        'name': 'posts',
        'description': 'Posts endpoints'
    },
    {
        'name': 'likes',
        'description': 'Likes endpoints'
    },
]

app = FastAPI(
    title='Social for webtronics',
    description='Description',
    version='0.0.1',
    openapi_tags=tags_metadata,
)


app.include_router(users_router)
app.include_router(posts_router)
app.include_router(likes_router)
