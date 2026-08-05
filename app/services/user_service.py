from app.models.user import UserCreate, UserInDB, UserLogin
from app.services.security import get_password_hash
from app.repositories.user_repo import create_user
from app.services.security import verify_password
from app.repositories.user_repo import get_user_by_email
async def register_user(user_data: UserCreate):
    hashed_pwd = get_password_hash(user_data.password)
    db_user = UserInDB(
        name=user_data.name,
        email=user_data.email,
        hashed_password=hashed_pwd
    )
    created_user = await create_user(db_user)
    return created_user


async def authenticate_user(login_data: UserLogin):
    user = await get_user_by_email(login_data.email)
    if not user:
        return False
    password = login_data.password
    is_password_correct = verify_password(password, user.hashed_password)
    if not is_password_correct:
        return False
    return user
