from repositories.base_repository import BaseRepository
from db.models.habit_log import HabitLog
from schemas.habit_log_schema import HabitLogCreate, HabitLogUpdate

class HabitLogRepository(BaseRepository[HabitLog, HabitLogCreate, HabitLogUpdate]):
    def __init__(self):
        super().__init__(HabitLog)