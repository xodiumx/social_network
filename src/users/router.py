from fastapi import APIRouter

from .schemas import UserCreate, UserRead
from .utils import auth_backend, fastapi_users

current_user = fastapi_users.current_user()

router = APIRouter(
    prefix='/auth',
    tags=['auth']
)
router.include_router(
    fastapi_users.get_auth_router(auth_backend),
    prefix='/jwt',
    tags=['auth'],
)
router.include_router(
    fastapi_users.get_register_router(UserRead, UserCreate),
    prefix='',
    tags=['auth'],
)
