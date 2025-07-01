from hexagonal_architecture.core.user.models.user import User


class InMemoryUserRepository:
    items: list[User] = []

    async def insert(self, user: User) -> None:
        if await self.find_by_email(user.email):
            return
        self.items.append(user)

    async def find_by_email(self, email: str) -> User | None:
        return next((u for u in self.items if u.email == email), None)
