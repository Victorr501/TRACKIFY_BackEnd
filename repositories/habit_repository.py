from db import session
from repositories.base_repository import BaseRepository
from db.models.habits import Habit
from schemas.habit_schema import HabitCreate, HabitUpdate

class HabitRepository(BaseRepository[Habit, HabitCreate, HabitUpdate]):
    def __init__(self):
        super().__init__(Habit)

    def get_by_user(self, db: session, user_id: int) -> list[Habit]:
        """Return all habits that belong to the given user."""
        return db.query(self.model).filter(self.model.user_id == user_id).all()