from fastapi import Depends, HTTPException
from api.base_router import BaseRouter
from services.habit_log_service import HabitLogService
from db.models.habit_log import HabitLog
from schemas.habit_log_schema import HabitLogCreate, HabitLogUpdate, HabitLogRead
from db.session import get_db

habit_log_service = HabitLogService()
habit_log_router = BaseRouter[HabitLog, HabitLogCreate, HabitLogUpdate, HabitLogRead](
    service=habit_log_service,
    model_name="habit_logs"
).router