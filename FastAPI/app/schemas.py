from pydantic import BaseModel, EmailStr
from datetime import datetime
from typing import Optional

# restrict fields that user passed in.
class PostBase(BaseModel): 
    title:str
    content:str
    # rating: Optional[int] = None
class PostCreate(PostBase):
    pass

class UserOut(BaseModel):
    id:int
    email:EmailStr
    created_at:datetime
    class Config:
        #orm_mode = True
        from_attributes:True
# restrict fields that user passed out.
class Post(PostBase):
    # title:str
    # content:str
    id: int
    created_at:datetime
    owner_id:int
    owner:UserOut
    class Config:
        #orm_mode = True
        from_attributes:True


class UserCreate(BaseModel):
    email: EmailStr
    password: str

class UserLogin(BaseModel):
    email:EmailStr 
    password:str

class Token(BaseModel):
    access_token:str
    token_type:str

class TokenData(BaseModel):
    id:Optional[int] = None
    

