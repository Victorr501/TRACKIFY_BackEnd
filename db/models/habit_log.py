from sqlalchemy import Column, Integer, ForeignKey, Date, Boolean, Text, UniqueConstraint
from sqlalchemy.orm import relationship
from db.base import Base

class HabitLog(Base):
    __tablename__ = "habit_logs"
    
    id = Column(Integer, primary_key=True, index=True)
    habit_id = Column(Integer, ForeignKey("habits.id", ondelete="CASCADE"), nullable=False)
    date = Column(Date, nullable=False)
    completed = Column(Boolean, default=False)
    notes = Column(Text, nullable=True)
    
    __table_args__ = (UniqueConstraint("habit_id", "date", name="_habit_date_uc"),)
    
    habit = relationship("Habit", back_populates="logs")
