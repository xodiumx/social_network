from fastapi import APIRouter, Depends

from users.utils import fastapi_users
from users.models import User

from .schemas import CreatePostSchema, GetPostSchema, UpdatePostSchema
from .services import PostService

current_user = fastapi_users.current_user()


router = APIRouter(
    prefix='/posts',
    tags=['posts']
)


@router.get('', response_model=list[GetPostSchema])
async def get_all(
    user: User = Depends(current_user),
    service: PostService = Depends()
    ) -> list[GetPostSchema]:
    """Get all posts."""
    return await service.get_many_posts()


@router.get('/{post_id}', response_model=GetPostSchema)
async def get_one(
    post_id: int,
    user: User = Depends(current_user),
    service: PostService = Depends()
    ) -> GetPostSchema:
    """Get a single post."""
    return await service.get_one_post(post_id=post_id)


@router.post('', response_model=CreatePostSchema)
async def create(
    data: CreatePostSchema,
    user: User = Depends(current_user),
    service: PostService = Depends()
    ) -> CreatePostSchema:
    """Post creation."""
    return await service.create_post(user_id=user.id, data=data)


@router.patch('/{post_id}')
async def update(
    post_id: int,
    data: CreatePostSchema,
    user: User = Depends(current_user),
    service: PostService = Depends()
    ) -> str:
    """Post update"""
    await service.update_post(
        post_id=post_id,
        user_id=user.id,
        data=data
        )
    return 'Post updated successfully'


@router.delete('/{post_id}')
async def delete(
    post_id: int,
    user: User = Depends(current_user),
    service: PostService = Depends()
    ) -> str:
    """Post removal"""
    await service.delete_post(post_id=post_id, user_id=user.id)
    return 'Post deleted successfully'
