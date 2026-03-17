from sqlalchemy.orm import DeclarativeBase


# будут наследоваться модели от этого класса Base
# добавлю сюда автоматические имена таблиц
class Base(DeclarativeBase):
    # если нет своего table_name называет модель именем класса
    @classmethod
    def __declare_last__(cls):
        if not hasattr(cls, "__tablename__"):
            cls.__tablename__ = cls.__name__.lower()
