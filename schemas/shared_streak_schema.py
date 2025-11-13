from datetime import date, datetime
from typing import Optional
from pydantic import BaseModel, Field


class SharedStreakBase(BaseModel):
    current_streak: int = Field(default=0, ge=0)
    max_streak: int = Field(default=0, ge=0)
    last_day_checked: Optional[date] = None


class SharedStreakCreate(SharedStreakBase):
    user1_id: int
    user2_id: int


class SharedStreakUpdate(BaseModel):
    current_streak: Optional[int] = Field(default=None, ge=0)
    max_streak: Optional[int] = Field(default=None, ge=0)
    last_day_checked: Optional[date] = None


class SharedStreakRead(SharedStreakBase):
    id: int
    user1_id: int
    user2_id: int
    created_at: datetime

    class Config:
        from_attributes = True
