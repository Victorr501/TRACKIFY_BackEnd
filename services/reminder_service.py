from services.base_service import BaseService
from repositories.reminder_repository import ReminderRepository
from db.models.reminder import Reminder
from schemas.reminder_schema import ReminderCreate, ReminderUpdate
from sqlalchemy.orm import Session

class ReminderService(BaseService[Reminder, ReminderCreate, ReminderUpdate]):
    def __init__(self):
        super().__init__(ReminderRepository())
    
    