from pydantic import BaseModel
from datetime import date
from typing import Optional

class HabitLogBase(BaseModel):
    date: date
    completed: bool = False
    notes: Optional[str] = None


class HabitLogCreate(HabitLogBase):
    habit_id: int
    

class HabitLogUpdate(BaseModel):
    date: Optional[date] = None
    completed: Optional[bool] = None
    notes: Optional[str] = None
    

class HabitLogRead(HabitLogBase):
    id: int
    habit_id: int
    
    class Config:
        from_attributes = True
        

class HabitLogSummary(BaseModel):
    total_logs: int
    completed_logs: int
    pending_logs: int
    completion_rate: float
        
