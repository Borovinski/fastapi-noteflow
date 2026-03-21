from pydantic import BaseModel
from typing import List, Optional
import uuid

from backend.app.schemas.note import NoteRead


class TagBase(BaseModel):
    name: str


class TagCreate(BaseModel):
    pass


# Схема обновления Tag (частичное)
class TagUpdate(BaseModel):
    name: Optional[str]


# Схема чтения Tag
class TagRead(TagBase):
    id: uuid.UUID
    notes: List[NoteRead] = []  # список заметок для этого тега

    class Config:
        orm_mode = True
