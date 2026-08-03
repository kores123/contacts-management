from app.database import db
from app.models.user import UserInDB

async def create_user(user: UserInDB):
    user_dict = user.model_dump()
    result = await db.users.insert_one(user_dict)
    user_dict["id"] = str(result.inserted_id)
    return user_dict