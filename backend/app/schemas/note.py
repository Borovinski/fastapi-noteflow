from pydantic import BaseModel
from typing import List, Optional
from datetime import datetime
import uuid

from backend.app.schemas.tag import TagRead


class NoteBase(BaseModel):
    title: str
    content: str


class NoteCreate(NoteBase):
    user_id: uuid.UUID
    tag_ids: Optional[List[uuid.UUID]] = []


class NoteUpdate(BaseModel):
    title: Optional[str]
    content: Optional[str]
    tag_ids: Optional[List[uuid.UUID]] = []


class NoteRead(NoteBase):
    id: uuid.UUID
    created_at: datetime
    user_id: uuid.UUID
    tags: List[TagRead] = []

    class Config:
        orm_mode = True
