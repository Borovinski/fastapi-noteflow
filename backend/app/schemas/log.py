# Схема создания лога
import datetime
import uuid
from pydantic import BaseModel


class LogCreate(BaseModel):
    user_id: uuid.UUID
    note_id: uuid.UUID
    action: str


# Схема чтения лога
class LogRead(BaseModel):
    id: uuid.UUID
    user_id: uuid.UUID
    note_id: uuid.UUID
    action: str
    timestamp: datetime.datetime

    class Config:
        orm_mode = True
