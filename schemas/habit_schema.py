from pydantic import BaseModel
from typing import Optional, List
from datetime import datetime
from schemas.habit_log_schema import HabitLogRead
from schemas.reminder_schema import ReminderRead

class HabitBase(BaseModel):
    name: str
    description: Optional[str] = None
    frequency: str #"daily" o "weekly"
    target_day: Optional[list[int]] = None
    color: Optional[str] = None
    icon: Optional[str] = None
    is_active: Optional[bool] = True
    
class HabitCreate(HabitBase):
    user_id: int
    
class HabitUpdate(BaseModel):
    name: Optional[str] = None
    description: Optional[str] = None
    frequency: Optional[str] = None
    target_days: Optional[list[int]] = None
    color: Optional[str] = None
    icon: Optional[str] = None
    is_active: Optional[bool] = None
    
class HabitRead(HabitBase):
    id: int
    created_at: datetime
    logs: List[HabitLogRead] = []
    remiders: List[ReminderRead] = []
    
    class Config:
        from_attributes = True