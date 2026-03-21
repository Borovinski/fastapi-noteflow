import hashlib
from sqlalchemy.orm import Session
from typing import List, Optional
from app.models.user import User
from app.repositories.user_repository import UserRepository
from app.schemas.user import UserRead, UserCreate, UserUpdate


class UserService:
    def __init__(self, db: Session):
        self.repository = UserRepository(db)

    def _hash_password(self, password: str) -> str:
        return hashlib.sha256(password.encode()).hexdigest()

    def create_user(self, user_data: UserCreate) -> User:
        # Проверка, есть ли пользователь с таким email
        existing_user = self.repository.get_by_email(user_data.email)
        if existing_user:
            raise ValueError("User with this email already exists")

        # Хешируем пароль
        user_dict = user_data.model_dump()
        user_dict["password"] = self._hash_password(user_data.password)

        # Создаём пользователя через репозиторий
        return self.repository.create(UserCreate(**user_dict))

    # Получить пользователя по id
    def get_user(self, user_id: int) -> Optional[User]:
        return self.repository.get_by_id(user_id)

    # Обновить пользователя
    def update_user(self, user_id: int, user_data: UserUpdate) -> User:
        user = self.repository.get_by_id(user_id)
        if not user:
            raise ValueError("User not found")

        # Если обновляют пароль — хешируем
        if user_data.password:
            user_data.password = self._hash_password(user_data.password)

        return self.repository.update(user, user_data)

    # Удалить пользователя
    def delete_user(self, user_id: int) -> None:
        user = self.repository.get_by_id(user_id)
        if not user:
            raise ValueError("User not found")
        self.repository.delete(user)
