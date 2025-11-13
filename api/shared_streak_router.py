from typing import List
from fastapi import Depends, HTTPException

from api.base_router import BaseRouter
from db import session
from services.shared_streak_service import SharedStreakService
from db.models.shared_streak import SharedStreak
from schemas.shared_streak_schema import (
    SharedStreakCreate,
    SharedStreakUpdate,
    SharedStreakRead,
)

shared_streak_service = SharedStreakService()
shared_streak_router = BaseRouter[
    SharedStreak,
    SharedStreakCreate,
    SharedStreakUpdate,
    SharedStreakRead,
](
    service=shared_streak_service,
    model_name="shared-streaks",
    read_schema=SharedStreakRead,
    create_schema=SharedStreakCreate,
    update_schema=SharedStreakUpdate,
).router


@shared_streak_router.get("/user/{user_id}", response_model=List[SharedStreakRead])
def get_user_shared_streaks(user_id: int, db: session = Depends(session.get_db)):
    streaks = shared_streak_service.get_by_user(db, user_id)
    return [SharedStreakRead.model_validate(streak, from_attributes=True) for streak in streaks]


@shared_streak_router.get("/users/{user1_id}/{user2_id}", response_model=SharedStreakRead)
def get_shared_streak_between_users(
    user1_id: int,
    user2_id: int,
    db: session = Depends(session.get_db),
):
    streak = shared_streak_service.get_by_user_pair(db, user1_id, user2_id)
    if not streak:
        raise HTTPException(status_code=404, detail="Shared streak not found for the provided users")
    return SharedStreakRead.model_validate(streak, from_attributes=True)