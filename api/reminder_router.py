from fastapi import Depends, HTTPException
from api.base_router import BaseRouter
from services.reminder_service import ReminderService
from db.models.reminder import Reminder
from schemas.reminder_schema import ReminderCreate, ReminderUpdate, ReminderRead
from db.session import get_db

reminder_service = ReminderService()
reminder_router = BaseRouter[Reminder, ReminderCreate, ReminderUpdate, ReminderRead](
    service=reminder_service,
    model_name="reminders",
    read_schema=ReminderRead,
    create_schema=ReminderCreate,
    update_schema=ReminderUpdate
).router