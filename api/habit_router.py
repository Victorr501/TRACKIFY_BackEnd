from typing import List
from fastapi import Depends, HTTPException
from api.base_router import BaseRouter
from db import session
from services.habit_service import HabitService
from db.models.habits import Habit
from schemas.habit_schema import HabitCreate, HabitUpdate, HabitRead

habit_service = HabitService()
habit_router = BaseRouter[Habit, HabitCreate, HabitUpdate, HabitRead](
    service=habit_service,
    model_name="habits",
    read_schema=HabitRead,
    create_schema=HabitCreate,
    update_schema=HabitUpdate
).router

@habit_router.get("/user/{user_id}", response_model=List[HabitRead])
def get_user_habits(user_id: int, db: session = Depends(session.get_db)):
    try:
        habits = habit_service.get_user_habits(db, user_id)
    except ValueError as exc:
        raise HTTPException(status_code=400, detail=str(exc)) from exc
    return [HabitRead.model_validate(habit, from_attributes=True) for habit in habits]