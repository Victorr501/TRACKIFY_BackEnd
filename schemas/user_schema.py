from pydantic import BaseModel, EmailStr, Field
from typing import Optional, List
from datetime import datetime


class UserBase(BaseModel):
    username: str
    email: EmailStr
    bio: Optional[str] = None
    timezone: Optional[str] = "Europe/Madrid"
    
class UserCreate(UserBase):
    password: str
    
class UserUpdate(BaseModel):
    username: Optional[str] = Field(None)
    email: Optional[EmailStr] = Field(None)
    bio: Optional[str] = Field(None)
    timezone: Optional[str] = Field("Europe/Madrid")
    notifications_enable: Optional[bool] = Field(None)
    is_active: Optional[bool] = Field(None)
    last_login: Optional[datetime] = Field(None)
    update_at: Optional[datetime] = Field(None)
    streak_count: Optional[int] = Field(None)
    max_streak: Optional[int] = Field(None)

    class Config:
        from_attributes = True
    
    
class UserRead(UserBase):
    id: int
    streak_count: int
    max_streak: int
    notifications_enable: bool
    is_active: bool
    last_login: Optional[datetime] = None
    created_at: datetime
    update_at: datetime
    class Config:
        from_attributes = True
        
class UserPasswordUpdate(BaseModel):
    old_password: str
    new_password: str
    
class UserDelete(BaseModel):
    password: str