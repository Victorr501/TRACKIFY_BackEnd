from typing import List, Optional
from db import session
from services.base_service import BaseService
from repositories.habit_repository import HabitRepository
from db.models.habits import Habit
from schemas.habit_schema import HabitCreate, HabitUpdate

class HabitService(BaseService[Habit, HabitCreate, HabitUpdate]):
    def __init__(self):
        repository = HabitRepository()
        super().__init__(repository)
        self.repository: HabitRepository = repository

    def get_user_habits(self, db: session, user_id: Optional[int]) -> List[Habit]:
        if not user_id:
            raise ValueError("Se requiere el ID del usuario para obtener sus hábitos.")
        return self.repository.get_by_user(db, user_id)