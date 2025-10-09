from repositories.base_repository import BaseRepository
from db.models.user import User
from schemas.user_schema import UserCreate, UserUpdate

class UserRepository(BaseRepository[User, UserCreate, UserUpdate]):
    def __init__(self):
        super().__init__(User)
        
    