# app/models/note.py
import uuid
from datetime import datetime
from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy import DateTime, String, ForeignKey
from app.db.base import Base

from typing import TYPE_CHECKING

# Импорт таблицы-связки для runtime!
from app.models.note_tag import note_tags

if TYPE_CHECKING:
    from .user import User
    from .tag import Tag
    from .log import Log


class Note(Base):
    __tablename__ = "notes"

    id: Mapped[uuid.UUID] = mapped_column(
        UUID(as_uuid=True), primary_key=True, default=uuid.uuid4
    )
    title: Mapped[str] = mapped_column(String, nullable=False)
    content: Mapped[str] = mapped_column(String, nullable=False)
    created_at: Mapped[datetime] = mapped_column(DateTime, default=datetime.utcnow)

    # FK на пользователя
    user_id: Mapped[uuid.UUID] = mapped_column(
        UUID(as_uuid=True), ForeignKey("users.id")
    )
    user: Mapped["User"] = relationship(back_populates="notes")

    # связь с тегами через association table
    tags: Mapped[list["Tag"]] = relationship(
        "Tag", secondary=note_tags, back_populates="notes"
    )

    # связь с логами
    logs: Mapped[list["Log"]] = relationship(
        "Log", back_populates="note", cascade="all, delete-orphan"
    )
