# app/models/tag.py
import uuid
from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy import String
from app.db.base import Base

from typing import TYPE_CHECKING

# Импорт таблицы-связки для runtime!
from app.models.note_tag import note_tags

if TYPE_CHECKING:
    from .note import Note


class Tag(Base):
    __tablename__ = "tags"

    id: Mapped[uuid.UUID] = mapped_column(
        UUID(as_uuid=True), primary_key=True, default=uuid.uuid4
    )
    name: Mapped[str] = mapped_column(String, unique=True, nullable=False)

    # связь с заметками через association table
    notes: Mapped[list["Note"]] = relationship(
        "Note", secondary=note_tags, back_populates="tags"
    )
