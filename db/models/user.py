from sqlalchemy import Column, Integer, String, Boolean, DateTime, Text
from sqlalchemy.orm import relationship
from datetime import datetime
from db.base import Base

class User(Base):
    __tablename__ = "users"
    
    id = Column(Integer, primary_key=True, index=True)
    username = Column(String(50), unique=True, nullable=False)
    email = Column(String(100), unique=True, nullable=False)
    password = Column(String(255), nullable=False)
    
    bio = Column(Text, nullable=True)
    timezone = Column(String(50), default="Europe/Madrid")
    
    streak_count = Column(Integer, default=0)
    max_streak = Column(Integer, default=0)
    
    notifications_enable = Column(Boolean, default=True)
    is_active = Column(Boolean, default=True)
    
    last_login = Column(DateTime, nullable=True)
    created_at = Column(DateTime, default=datetime.utcnow)
    update_at = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)
    
    #Relaciones
    habits = relationship("Habit", back_populates="user", cascade="all, delete-orphan")
    