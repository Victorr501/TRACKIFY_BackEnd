from datetime import date
from typing import List, Optional
from services.base_service import BaseService
from repositories.habit_log_repository import HabitLogRepository
from db.models.habit_log import HabitLog
from schemas.habit_log_schema import HabitLogCreate, HabitLogUpdate
from sqlalchemy.orm import Session

class HabitLogService(BaseService[HabitLog, HabitLogCreate, HabitLogUpdate]):
    def __init__(self):
        repository = HabitLogRepository()
        super().__init__(repository)
        self.repository: HabitLogRepository = repository

    def get_user_logs(self, db: Session, user_id: Optional[int]) -> List[HabitLog]:
        if not user_id:
            raise ValueError("Se requiere el ID del usuario para obtener sus registros.")
        return self.repository.get_by_user(db, user_id)

    def get_summary(
        self,
        db: Session,
        *,
        user_id: Optional[int] = None,
        habit_id: Optional[int] = None,
        start_date: Optional[date] = None,
        end_date: Optional[date] = None,
    ) -> dict[str, float | int]:
        if start_date and end_date and start_date > end_date:
            raise ValueError("La fecha de inicio no puede ser posterior a la fecha de fin.")

        return self.repository.get_summary(
            db,
            user_id=user_id,
            habit_id=habit_id,
            start_date=start_date,
            end_date=end_date,
        )