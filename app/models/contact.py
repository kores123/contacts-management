from datetime import datetime
from typing import Optional
from pydantic import BaseModel, Field


class ContactBase(BaseModel):
  name: str
  phone: str
  email: Optional[str] = None


class ContactCreate(ContactBase):
  pass


class ContactResponse(ContactBase):
  id: str = Field(..., alias="_id")
  created_at: datetime

  class Config:
    populate_by_name = True