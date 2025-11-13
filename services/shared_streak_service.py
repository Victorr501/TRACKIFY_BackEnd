from typing import List, Optional
from sqlalchemy.orm import Session

from services.base_service import BaseService
from repositories.shared_streak_repository import SharedStreakRepository
from db.models.shared_streak import SharedStreak
from schemas.shared_streak_schema import SharedStreakCreate, SharedStreakUpdate


class SharedStreakService(BaseService[SharedStreak, SharedStreakCreate, SharedStreakUpdate]):
    def __init__(self) -> None:
        repository = SharedStreakRepository()
        super().__init__(repository)
        self.repository: SharedStreakRepository = repository

    def get_by_user(self, db: Session, user_id: int) -> List[SharedStreak]:
        return self.repository.get_by_user(db, user_id)

    def get_by_user_pair(self, db: Session, user1_id: int, user2_id: int) -> Optional[SharedStreak]:
        return self.repository.get_by_user_pair(db, user1_id, user2_id)
