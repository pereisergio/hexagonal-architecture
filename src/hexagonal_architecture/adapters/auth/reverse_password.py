"""
Na arquitetura Hexagonal esta classe é um Adaptador!
O adaptador NÂO faz parte do core da aplicação
"""

from hexagonal_architecture.core.user.services.criptograph_provider import (
    CriptographProvider,
)


class ReversePassword(CriptographProvider):
    def criptograph(self, password: str) -> str:
        """
        Reverse the given password string.

        :param password: The password to be reversed.
        :return: The reversed password.
        """
        return "".join(reversed(password))
