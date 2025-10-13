from api.base_router import BaseRouter
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