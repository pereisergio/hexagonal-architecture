from hexagonal_architecture.core.shared.erros import Erros
from hexagonal_architecture.core.shared.id import Id
from hexagonal_architecture.core.shared.use_case import UseCase
from hexagonal_architecture.core.user.models.user import User
from hexagonal_architecture.core.user.services.criptograph_provider import (
    CriptographProvider,
)
from hexagonal_architecture.core.user.services.user_repository import UserRepository


class UserRegister(UseCase[User, None]):
    def __init__(
        self, user_repository: UserRepository, criptograph_provider: CriptographProvider
    ):
        """
        Inicializa o caso de uso de registro de usuário.

        :param criptograph_provider: Provedor de criptografia a ser usado para criptografar senhas.
        """
        self.__criptograph_provider = criptograph_provider
        self.__repository = user_repository

    async def execute(self, user: User) -> None:
        cripto_password = self.__criptograph_provider.criptograph(user.password)

        user_exists = self.__repository.find_by_email(user.email)
        if user_exists:
            raise ValueError(Erros.USER_ALREADY_EXISTS)

        user.user_id = (Id.generate_hash(),)
        user.password = cripto_password

        self.__repository.insert(user)
