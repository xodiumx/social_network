from fastapi import Depends, HTTPException, status
from sqlalchemy import delete, insert, select, update
from sqlalchemy.ext.asyncio import AsyncSession

from main.db import get_async_session

from .models import posts
from .schemas import CreatePostSchema, UpdatePostSchema


class PostService:

    def __init__(
            self,
            session: AsyncSession = Depends(get_async_session)) -> None:
        """Creating a new session."""
        self.session = session
    
    async def get_many_posts(self) -> list[posts]:
        """Get a list of all posts."""
        query = select(posts)
        response = await self.session.execute(query)
        return response.all()

    async def get_one_post(self, post_id: int) -> posts:
        """
        Get a single post function
        - if post does not exist raise an exception
        """
        query = select(posts).filter_by(id=post_id)
        response = await self.session.execute(query)
        post = response.first()
        if not post:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail='Post does not exist'
            )
        return post

    async def create_post(
            self,
            user_id: int,
            data: CreatePostSchema) -> None:
        """
        Create post function
        attributes:
            - user_id: id of current user
            - text: text of post
        """
        new_post = data.dict()
        new_post['author'] = user_id
        statement = insert(posts).values(**new_post)
        await self.session.execute(statement)
        await self.session.commit()
        return new_post
    
    async def update_post(
            self,
            post_id: int,
            user_id: int,
            data: UpdatePostSchema):
        """
        Update post function
          - Filter the post by author and by id
          - save the new text in the post
        """
        query = (
            update(posts)
            .filter_by(id=post_id, author=user_id)
            .values(text=data.text)
        )
        await self.session.execute(query)
        await self.session.commit()
        # TODO: add new time
    
    async def delete_post(
            self,
            post_id: int,
            user_id: int) -> None:
        """
        Delete post function
          - Filter the post by author and by id
        """
        query = (
            delete(posts)
            .filter_by(id=post_id, author=user_id)
        )
        await self.session.execute(query)
        await self.session.commit()
