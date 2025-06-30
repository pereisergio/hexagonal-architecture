from hexagonal_architecture.core.shared.use_case import UseCase
from hexagonal_architecture.core.user.models.user import User


class UserRegister(UseCase[User, None]):
    async def execute(self, entry: User) -> None:
        pass
