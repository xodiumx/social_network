from fastapi import Depends
from fastapi_users import FastAPIUsers
from fastapi_users.db import SQLAlchemyUserDatabase
from fastapi_users.authentication import (
    AuthenticationBackend, CookieTransport, JWTStrategy, )
from sqlalchemy.ext.asyncio import AsyncSession

from main.db import get_async_session
from main.settings import settings

from .models import User
from .manage import UserManager


SECRET = settings.secret_key


def get_jwt_strategy() -> JWTStrategy:
    """Get JWT token."""
    return JWTStrategy(secret=SECRET, lifetime_seconds=3600)


async def get_user_db(session: AsyncSession = Depends(get_async_session)):
    yield SQLAlchemyUserDatabase(session, User)


async def get_user_manager(user_db=Depends(get_user_db)):
    yield UserManager(user_db)


cookie_transport = CookieTransport(
    cookie_name='auth', cookie_max_age=3600)

auth_backend = AuthenticationBackend(
    name='jwt',
    transport=cookie_transport,
    get_strategy=get_jwt_strategy,
)

fastapi_users = FastAPIUsers[User, int](
    get_user_manager,
    [auth_backend],
)