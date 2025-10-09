from repositories.base_repository import BaseRepository
from db.models.habits import Habit
from schemas.habit_schema import HabitCreate, HabitUpdate

class HabitRepository(BaseRepository[Habit, HabitCreate, HabitUpdate]):
    def __init__(self):
        super().__init__(Habit)