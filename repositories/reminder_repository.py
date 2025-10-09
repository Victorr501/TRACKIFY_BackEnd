from repositories.base_repository import BaseRepository
from db.models.reminder import Reminder
from schemas.reminder_schema import ReminderCreate, ReminderUpdate

class ReminderRepository(BaseRepository[Reminder, ReminderCreate, ReminderUpdate]):
    def __init__(self):
        super().__init__(Reminder)