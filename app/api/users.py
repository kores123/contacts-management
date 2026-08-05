from fastapi import APIRouter, HTTPException
from app.models.user import UserCreate, UserResponse, UserLogin
from app.services.user_service import register_user, authenticate_user
from app.services.security import create_access_token
router = APIRouter()

@router.post("/register", response_model=UserResponse)
async def create_user(user: UserCreate):
    return await register_user(user)

@router.post("/login")
async def login_user(user: UserLogin):
    authenticated_user = await authenticate_user(user)
    if not authenticated_user:
        raise HTTPException(status_code=401, detail="Nieprawidłowy email lub hasło")

    access_token = create_access_token(data={"sub": authenticated_user.email})
    return {"access_token": access_token, "token_type": "bearer"}

