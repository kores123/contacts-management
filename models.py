from typing import Optional
from pydantic import BaseModel, Field
from datetime import datetime
class Contact(BaseModel):
    id: int
    name: str
    last_name: str
    phone_number: Optional[int] = None
    created_at: datetime = Field(default_factory=datetime.now)