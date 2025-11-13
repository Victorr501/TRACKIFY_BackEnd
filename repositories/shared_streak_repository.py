from typing import List, Optional
from sqlalchemy.orm import Session

from repositories.base_repository import BaseRepository
from db.models.shared_streak import SharedStreak
from schemas.shared_streak_schema import SharedStreakCreate, SharedStreakUpdate


class SharedStreakRepository(BaseRepository[SharedStreak, SharedStreakCreate, SharedStreakUpdate]):
    def __init__(self) -> None:
        super().__init__(SharedStreak)

    def get_by_user(self, db: Session, user_id: int) -> List[SharedStreak]:
        """Return every shared streak where the given user participates."""
        return (
            db.query(self.model)
            .filter((self.model.user1_id == user_id) | (self.model.user2_id == user_id))
            .all()
        )

    def get_by_user_pair(self, db: Session, user1_id: int, user2_id: int) -> Optional[SharedStreak]:
        """Return a shared streak between the provided users regardless of order."""
        return (
            db.query(self.model)
            .filter(SharedStreak.by_user_pair_filter(user1_id, user2_id))
            .first()
        )
