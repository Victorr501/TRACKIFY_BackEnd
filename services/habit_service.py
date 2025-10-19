from services.base_service import BaseService
from repositories.habit_repository import HabitRepository
from db.models.habits import Habit
from schemas.habit_schema import HabitCreate, HabitUpdate

class HabitService(BaseService[Habit, HabitCreate, HabitUpdate]):
    def __init__(self):
        repository = HabitRepository()
        super().__init__(repository)