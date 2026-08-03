from fastapi import APIRouter, HTTPException
from app.models.user import UserCreate, UserResponse
from app.services.user_service import register_user
from app.services.security import verify_password, create_access_token

router = APIRouter()

@router.post("/register", response_model=UserResponse)
async def create_user(user: UserCreate):
    return await register_user(user)


