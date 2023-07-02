from fastapi import FastAPI

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
]

app = FastAPI(
    title='Social for webtronics',
    description='Description',
    version='0.0.1',
    openapi_tags=tags_metadata,
)


app.include_router(users_router)