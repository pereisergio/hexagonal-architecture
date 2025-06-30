from hexagonal_architecture.core.shared.use_case import UseCase
from hexagonal_architecture.core.user.models.user import User


class UserRegister(UseCase[User, None]):
    async def execute(self, user: User) -> None:
        cripto_password = "".join(reversed(user.password))
        print(cripto_password)
