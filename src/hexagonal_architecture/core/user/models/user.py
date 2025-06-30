from abc import ABC, abstractmethod


class User(ABC):
    @abstractmethod
    def __init__(self, user_id: str, name: str, email: str, password: str):
        self.id: str = user_id
        self.name: str = name
        self.email: str = email
        self.password: str = password


class ConcreteUser(User):
    def __init__(self, user_id: str, name: str, email: str, password: str):
        super().__init__(user_id, name, email, password)
