from fastapi import Depends, HTTPException, status
from sqlalchemy import delete, insert, select
from sqlalchemy.exc import IntegrityError
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.sql.schema import Table

from main.db import get_async_session
from posts.models import posts

from .models import dislikes, likes


class BaseService:

    def __init__(
            self,
            session: AsyncSession = Depends(get_async_session)) -> None:
        """Creating a new session."""
        self.session = session
    
    async def is_own_post(
            self,
            post_id: int,
            user_id: int,
            action: str) -> bool:
        query_own_post = (
            select(posts)
            .filter_by(author=user_id, id=post_id)
        )
        own_post = await self.session.execute(query_own_post)
        if not own_post.first():
            return True
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=f'{action} cannot be used with your own post')

    async def like_exists(
            self,
            post_id: int,
            user_id: int,
            table: Table,
            action: str) -> bool:
        query_like_exists = (
            select(table)
            .filter_by(author=user_id, post=post_id)
        )
        like_exists = await self.session.execute(query_like_exists)
        if not like_exists.first():
            return True
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=f'{action} already used')

    async def add(
            self,
            post_id: int,
            user_id: int,
            table: Table) -> bool:
        """
        Add a like or dislike to the post:
        - action depends on the table name
        - if it is your own post, raise an exception
        - if like or dislike has already been added, raise an exception
        - if like or dislike successfully added returns True
        """
        action = 'Like' if table == likes else 'Dislike'

        not_own = await self.is_own_post(post_id, user_id, action)
        not_exists = await self.like_exists(post_id, user_id, table, action)

        if all((not_own, not_exists)):
            query_adding_like = (
                insert(table)
                .values(author=user_id, post=post_id)
            )
            try:
                await self.session.execute(query_adding_like)
                await self.session.commit()
            except IntegrityError:
                raise HTTPException(
                    status_code=status.HTTP_404_NOT_FOUND,
                    detail='Post does not exist'
                )
            return True
        return False

    async def delete(
            self,
            post_id: int,
            user_id: int,
            table: Table):
        """
        Remove a like or dislike from the post:
        - action depends on the table name
        """
        query = (
            delete(table)
            .filter_by(author=user_id, post=post_id)
        )
        await self.session.execute(query)
        await self.session.commit()
        

class LikeService(BaseService):
    
    async def add_like_to_post(
            self,
            post_id: int,
            user_id: int) -> bool:
        """Method of adding likes."""
        table = likes
        return await self.add(post_id, user_id, table)

    async def remove_like_from_post(
            self,
            post_id: int,
            user_id: int):
        """Method of removing likes."""
        table = likes
        return await self.delete(post_id, user_id, table)


class DisLikeService(BaseService):
    
    async def add_dislike_to_post(
            self,
            post_id: int,
            user_id: int) -> bool:
        """Method of adding dislikes."""
        table = dislikes
        return await self.add(post_id, user_id, table)
    
    async def remove_dislike_from_post(
            self,
            post_id: int,
            user_id: int):
        """Method of removing dislikes"""
        table = dislikes
        return await self.delete(post_id, user_id, table)
