from pydantic import BaseModel


class BasePostSchema(BaseModel):
    text: str

    class Config:
        orm_mode = True


class GetPostSchema(BasePostSchema):
    author: int
    created_at: str


class CreatePostSchema(BasePostSchema):
    ...


class UpdatePostSchema(BasePostSchema):
    created_at: str
