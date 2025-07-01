from hexagonal_architecture.core.user.services.criptograph_provider import (
    CriptographProvider,
)


class SpacePassword(CriptographProvider):
    def criptograph(self, password: str) -> str:
        """
        Space the given password string by adding spaces between characters.

        :param password: The password to be spaced.
        :return: The spaced password.
        """
        return " ".join(password)
