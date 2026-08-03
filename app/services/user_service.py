from app.models.user import UserCreate, UserInDB
from app.services.security import get_password_hash
from app.repositories.user_repo import create_user
async def register_user(user_data: UserCreate):
    hashed_pwd = get_password_hash(user_data.password)
    db_user = UserInDB(
        name=user_data.name,
        email=user_data.email,
        hashed_password=hashed_pwd
    )
    created_user = await create_user(db_user)
    return created_user