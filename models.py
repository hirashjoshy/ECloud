from pydantic import BaseModel
from typing import Optional

class AddUser(BaseModel):
    username: str
    password: str

class UpdateUser(BaseModel):
    username: Optional[str] = None
    password: Optional[str] = None