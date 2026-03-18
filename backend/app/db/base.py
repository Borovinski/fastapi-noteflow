from sqlalchemy.orm import DeclarativeBase


# будут наследоваться модели от этого класса Base
# добавлю сюда автоматические имена таблиц
class Base(DeclarativeBase):
    # если нет своего table_name называет модель именем класса
    @classmethod
    def __declare_last__(cls):
        if not hasattr(cls, "__tablename__"):
            cls.__tablename__ = cls.__name__.lower()

    # метод для вывода
    def __repr__(self):
        cls = self.__class__.__name__
        attrs = ", ".join(
            f"{k}={getattr(self, k)!r}" for k in self.__mapper__.columns.keys()
        )
        return f"<{cls}({attrs})>"
