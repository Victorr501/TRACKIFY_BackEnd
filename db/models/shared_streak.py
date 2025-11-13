from sqlalchemy import Column, Integer, ForeignKey, Date, DateTime
from sqlalchemy.orm import relationship
from datetime import datetime
from db.base import Base

class shared_streak(Base):
    __tablename__ = "shared_streaks"
    
    id = Column(Integer, primary_key=True, index=True)
    
    user1_id = Column(Integer, ForeignKey("users.id"), nullable=False)
    user2_id = Column(Integer, ForeignKey("users.id"), nullable=False)
    
    current_streak = Column(Integer, default=0)
    max_streak = Column(Integer, default=0)
    
    las_day_checked = Column(Date, nullable=True)
    
    created_at = Column(DateTime, default=datetime.utcnow)
    
    user1 = relationship("User", foreign_keys=[user1_id], back_populates="shared_streaks_as_user1")
    user2 = relationship("USer", foreign_keys=[user2_id], back_populates="shared_streaks_as_user2")
    
    