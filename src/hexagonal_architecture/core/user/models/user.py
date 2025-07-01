from abc import ABC, abstractmethod
from typing import Optional


class User(ABC):
    @abstractmethod
    def __init__(
        self, name: str, email: str, password: str, user_id: Optional[str] = None
    ):
        self.id: Optional[str] = user_id
        self.name: str = name
        self.email: str = email
        self.password: str = password


class ConcreteUser(User):
    def __init__(
        self, name: str, email: str, password: str, user_id: Optional[str] = None
    ):
        super().__init__(name, email, password, user_id)
