from pydantic import BaseModel
from typing import Optional
from datetime import time

class ReminderBase(BaseModel):
    time: time
    active: bool = True
    message: Optional[str] = None
    
class ReminderCreate(ReminderBase):
    habit_id: int
    
class ReminderUpdate(BaseModel):
    time: Optional[time] = None
    active: Optional[bool] = None
    message: Optional[str] = None
    
class ReminderRead(ReminderBase):
    id: int
    
    class Config:
        from_attributes = True