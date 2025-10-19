from pydantic import BaseModel, Field
from typing import Optional, List
from datetime import datetime
from schemas.habit_log_schema import HabitLogRead
from schemas.reminder_schema import ReminderRead

class HabitBase(BaseModel):
    name: str
    description: Optional[str] = Field(default=None)
    frequency: str #"daily" o "weekly"
    target_days: Optional[List[int]] = Field(default_factory=list)
    color: Optional[str] = Field(default=None)
    icon: Optional[str] = Field(default=None)
    is_active: Optional[bool] = Field(default=True)
    
class HabitCreate(HabitBase):
    user_id: int
    
class HabitUpdate(BaseModel):
    name: Optional[str] = None
    description: Optional[str] = None
    frequency: Optional[str] = None
    target_days: Optional[list[int]] = Field(default_factory=list)
    color: Optional[str] = None
    icon: Optional[str] = None
    is_active: Optional[bool] = None
    
class HabitRead(HabitBase):
    id: int
    user_id: int   
    created_at: datetime
    logs: List[HabitLogRead] = []
    reminders: List[ReminderRead] = []
    
    class Config:
        from_attributes = True