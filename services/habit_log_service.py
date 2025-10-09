from services.base_service import BaseService
from repositories.habit_log_repository import HabitLogRepository
from db.models.habit_log import HabitLog
from schemas.habit_log_schema import HabitLogCreate, HabitLogUpdate
from sqlalchemy.orm import Session

class HabitLogService(BaseService[HabitLog, HabitLogCreate, HabitLogUpdate]):
    def __init__(self):
        super().__init__(HabitLogRepository())