from abc import ABC, abstractmethod

from hexagonal_architecture.core.user.models.user import User


class UserRepository(ABC):
    """
    Interface for user repository.
    """

    @abstractmethod
    def insert(self, user: User) -> None:
        """
        Insert a new user into the repository.

        :param user: The user to insert.
        """
        pass

    @abstractmethod
    def find_by_email(self, email: str) -> User | None:
        """
        Find a user by email.

        :param email: The email of the user to find.
        :return: The user if found, otherwise None.
        """
        pass
