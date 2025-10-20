from datetime import date
from typing import List, Optional
from fastapi import Depends, HTTPException, Query
from sqlalchemy.orm import Session
from api.base_router import BaseRouter
from services.habit_log_service import HabitLogService
from db.models.habit_log import HabitLog
from schemas.habit_log_schema import HabitLogCreate, HabitLogSummary, HabitLogUpdate, HabitLogRead
from db.session import get_db

habit_log_service = HabitLogService()
habit_log_router = BaseRouter[HabitLog, HabitLogCreate, HabitLogUpdate, HabitLogRead](
    service=habit_log_service,
    model_name="habit_logs",
    read_schema=HabitLogRead,
    create_schema=HabitLogCreate,
    update_schema=HabitLogUpdate
).router

@habit_log_router.get("/user/{user_id}", response_model=List[HabitLogRead])
def get_user_logs(user_id: int, db: Session = Depends(get_db)):
    try:
        logs = habit_log_service.get_user_logs(db, user_id)
    except ValueError as exc:
        raise HTTPException(status_code=400, detail=str(exc)) from exc
    return [HabitLogRead.model_validate(log, from_attributes=True) for log in logs]


@habit_log_router.get("/summary", response_model=HabitLogSummary)
def get_summary(
    db: Session = Depends(get_db),
    user_id: Optional[int] = Query(default=None),
    habit_id: Optional[int] = Query(default=None),
    start_date: Optional[date] = Query(default=None),
    end_date: Optional[date] = Query(default=None),
):
    try:
        summary = habit_log_service.get_summary(
            db,
            user_id=user_id,
            habit_id=habit_id,
            start_date=start_date,
            end_date=end_date,
        )
    except ValueError as exc:
        raise HTTPException(status_code=400, detail=str(exc)) from exc
    return summary