"""
Na arquitetura hexagonal esta interface é uma Porta!
A porta faz parte do core da sua aplicação
"""

from abc import ABC, abstractmethod


class CriptographProvider(ABC):
    """
    Interface para criptografia de senhas.
    Esta interface define o contrato que deve ser seguido por qualquer implementação de criptografia.
    """

    @abstractmethod
    def criptograph(self, password: str) -> str:
        """
        Criptografa a senha fornecida.

        :param password: A senha a ser criptografada.
        :return: A senha criptografada.
        """
        pass
