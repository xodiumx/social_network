from fastapi import APIRouter, Depends

from users.models import User
from users.utils import fastapi_users

from .services import DisLikeService, LikeService

current_user = fastapi_users.current_user()


router = APIRouter(
    prefix='',
    tags=['likes']
)


@router.post('/like')
async def add_like(
        post_id: int,
        user: User = Depends(current_user),
        service: LikeService = Depends()):
    """Add a like."""
    like_added = await service.add_like_to_post(post_id, user.id)
    if like_added:
        return {'detail': 'Like successfully added'}
    # TODO: raise exception


@router.delete('/like_remove')
async def remove_like(
        post_id: int,
        user: User = Depends(current_user),
        service: LikeService = Depends()):
    """Remove a like."""
    await service.remove_like_from_post(post_id, user.id)
    return {'detail': 'Like successfully removed'}


@router.post('/dislike')
async def add_dislike(
        post_id: int,
        user: User = Depends(current_user),
        service: DisLikeService = Depends()):
    """Add dislike."""
    dislike_added = await service.add_dislike_to_post(post_id, user.id)
    if dislike_added:
        return {'detail': 'Dislike successfully added'}
    # TODO: raise exception


@router.delete('/dislike_remove')
async def remove_dislike(
        post_id: int,
        user: User = Depends(current_user),
        service: DisLikeService = Depends()):
    """Remove dislike."""
    await service.remove_dislike_from_post(post_id, user.id)
    return {'detail': 'Dislike successfully removed'}
