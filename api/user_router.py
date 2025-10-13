from api.base_router import BaseRouter
from services.user_service import UserService
from db.models.user import User
from schemas.user_schema import UserCreate, UserUpdate, UserRead

user_service = UserService()
user_router = BaseRouter[User, UserCreate, UserUpdate, UserRead](
    service=user_service,
    model_name="users",
    read_schema=UserRead,
    create_schema=UserCreate,
    update_schema=UserUpdate
    
).router