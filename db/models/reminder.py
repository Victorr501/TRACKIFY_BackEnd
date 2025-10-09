from sqlalchemy import Column, Integer, ForeignKey, Time, Boolean, String
from sqlalchemy.orm import relationship
from db.base import Base

class Reminder(Base):
    __tablename__ = "reminders"
    
    
    id = Column(Integer, primary_key=True, index=True)
    habit_id = Column(Integer, ForeignKey("habits.id", ondelete="CASCADE"), nullable=False)
    time = Column(Time, nullable=False)
    active = Column(Boolean, default=True)
    message = Column(String(200), nullable=True)
    
    habit = relationship("Habit", back_populates="reminders")
    