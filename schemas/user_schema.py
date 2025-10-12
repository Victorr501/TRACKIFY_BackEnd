from pydantic import BaseModel, EmailStr
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
    username: Optional[str] = None
    email:  Optional[EmailStr] = None
    bio: Optional[str] = None
    timezone: Optional[str] = None
    notifications_enable: Optional[bool] = None
    is_active: Optional[bool] = None
    last_login: Optional[datetime] = None
    update_at: Optional[datetime] = None    
    
    
class UserRead(UserBase):
    id: int
    username: str
    streak_count: int
    max_streak: int
    notifications_enable: bool
    is_active: bool
    last_login: Optional[datetime] = None
    created_at: datetime
    update_at: datetime
    
    class Config:
        from_attributes = True