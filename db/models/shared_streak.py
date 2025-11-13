from sqlalchemy import Column, Integer, ForeignKey, Date, DateTime, and_, or_
from sqlalchemy.orm import relationship
from datetime import datetime
from db.base import Base


class SharedStreak(Base):
    __tablename__ = "shared_streaks"

    id = Column(Integer, primary_key=True, index=True)

    user1_id = Column(Integer, ForeignKey("users.id"), nullable=False)
    user2_id = Column(Integer, ForeignKey("users.id"), nullable=False)

    current_streak = Column(Integer, default=0)
    max_streak = Column(Integer, default=0)

    last_day_checked = Column(Date, nullable=True)

    created_at = Column(DateTime, default=datetime.utcnow)

    user1 = relationship("User", foreign_keys=[user1_id], back_populates="shared_streaks_as_user1")
    user2 = relationship("User", foreign_keys=[user2_id], back_populates="shared_streaks_as_user2")


    @classmethod
    def by_user_pair_filter(cls, user1_id: int, user2_id: int):
        """Return a filter expression for matching the streak regardless of user order."""
        return or_(
            and_(cls.user1_id == user1_id, cls.user2_id == user2_id),
            and_(cls.user1_id == user2_id, cls.user2_id == user1_id),
        )
