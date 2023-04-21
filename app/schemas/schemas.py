from typing import List
from pydantic import BaseModel

#Article inside UserDisplay
class Article(BaseModel):
    title: str
    content: str
    pulbished: bool
    class config():
        orm_Mode = True

class UserBase(BaseModel):
    username: str
    email: str
    password: str

class UserDisplay(BaseModel):
    username: str
    email: str
    items: List[Article] = []
    class Config():
        orm_mode = True

class ArticleBase(BaseModel):
    title: str
    content: str
    published: bool
    creator_id: int
