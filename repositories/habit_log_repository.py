from datetime import date
from typing import Optional
from sqlalchemy import case, func
from sqlalchemy.orm import Session
from db.models.habit_log import HabitLog
from db.models.habits import Habit
from repositories.base_repository import BaseRepository
from schemas.habit_log_schema import HabitLogCreate, HabitLogUpdate

class HabitLogRepository(BaseRepository[HabitLog, HabitLogCreate, HabitLogUpdate]):
    def __init__(self):
        super().__init__(HabitLog)
        
    def get_by_user(self, db: Session, user_id: int) -> list[HabitLog]:
        return (
            db.query(self.model)
            .join(Habit, Habit.id == self.model.habit_id)
            .filter(Habit.user_id == user_id)
            .order_by(self.model.date.desc(), self.model.id.desc())
            .all()
        )

    def get_summary(
        self,
        db: Session,
        *,
        user_id: Optional[int] = None,
        habit_id: Optional[int] = None,
        start_date: Optional[date] = None,
        end_date: Optional[date] = None,
    ) -> dict[str, float | int]:
        query = db.query(
            func.count(self.model.id).label("total_logs"),
            func.sum(case((self.model.completed == True, 1), else_=0)).label("completed_logs"),  # noqa: E712
        )

        if user_id is not None:
            query = query.join(Habit, Habit.id == self.model.habit_id).filter(Habit.user_id == user_id)

        if habit_id is not None:
            query = query.filter(self.model.habit_id == habit_id)

        if start_date is not None:
            query = query.filter(self.model.date >= start_date)

        if end_date is not None:
            query = query.filter(self.model.date <= end_date)

        result = query.one()
        total_logs = int(result.total_logs or 0)
        completed_logs = int(result.completed_logs or 0)
        pending_logs = total_logs - completed_logs
        completion_rate = float(completed_logs / total_logs) if total_logs else 0.0

        return {
            "total_logs": total_logs,
            "completed_logs": completed_logs,
            "pending_logs": pending_logs,
            "completion_rate": completion_rate,
        }