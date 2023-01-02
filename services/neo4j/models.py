from datetime import datetime
from pydantic import BaseModel


class User(BaseModel):
    id: int
    name : str
    email: str
    update : list[datetime] | None =  []
    email: str
    facebook: str
    phone: int
