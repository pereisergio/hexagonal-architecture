from hexagonal_architecture.core.user.models.user import User
from hexagonal_architecture.core.user.services.user_repository import UserRepository


class InMemoryUserRepository(UserRepository):
    items: list[User] = []

    def insert(self, user: User) -> None:
        if self.find_by_email(user.email):
            return
        self.items.append(user)

    def find_by_email(self, email: str) -> User | None:
        return next((u for u in self.items if u.email == email), None)
