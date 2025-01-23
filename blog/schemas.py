from pydantic import BaseModel
from typing import Optional

class BlogBase(BaseModel):
    title : str
    body: str
    published: bool
    user_id: int
class UserBase(BaseModel):
    name: str

