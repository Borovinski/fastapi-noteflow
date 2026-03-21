import datetime
from typing import Optional
from uuid import UUID
from pydantic import BaseModel, EmailStr, Field, field_validator


# Базовая схема с общим полем
class UserBase(BaseModel):
    email: EmailStr


# схема создания пользователя
class UserCreate(UserBase):
    password: str = Field(
        ..., min_length=8, max_length=16, description="Пароль от 8 до 16 символов"
    )

    @field_validator("password")
    @classmethod
    def validate_password(cls, value: str) -> str:
        if not any(char.isdigit() for char in value):
            raise ValueError("Пароль доджен содержать хотя бы одну цифру")
        if not any(char.isalpha() for char in value):
            raise ValueError("Пароль должен содержать хотя бы одну букву")
        return value


# схема обновления пользователя
class UserUpdate(BaseModel):
    email: Optional[EmailStr] = None
    password: Optional[str] = Field(None, min_length=8, max_length=16)


class UserRead(UserBase):
    id: UUID
    created_at: datetime.datetime

    class Config:
        orm_mode = True
