from typing import Optional
from pydantic import BaseModel
class Contact(BaseModel):
    id: int
    name: str
    last_name: str
    phone_number: Optional[int] = None