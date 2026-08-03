from pydantic import BaseModel, EmailStr
class UserBase(BaseModel):
  name: str
  email: EmailStr
class UserCreate(UserBase):
    password: str
class UserInDB(UserBase):
    hashed_password: str
class UserResponse(UserBase):
 id: str

