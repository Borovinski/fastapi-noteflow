from datetime import datetime
import uuid

from pydantic import BaseModel


# Схема создания сессии
class SessionCreate(BaseModel):
    user_id: uuid.UUID
    token: str
    expires_at: datetime


# Схема чтения сессии
class SessionRead(BaseModel):
    id: uuid.UUID
    user_id: uuid.UUID
    token: str
    expires_at: datetime

    class Config:
        orm_mode = True
