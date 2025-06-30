from abc import ABC, abstractmethod
from typing import Generic, TypeVar

IN = TypeVar("IN")
OUT = TypeVar("OUT")


class UseCase(ABC, Generic[IN, OUT]):
    """
    Abstract base class for use cases in the hexagonal architecture.
    Use cases encapsulate the business logic and orchestrate the flow of data
    between the domain and the application layers.
    """

    @abstractmethod
    def execute(self, entry: IN) -> OUT:
        """
        Execute the use case with the provided arguments.
        This method should be implemented by subclasses to define the specific
        business logic for the use case.
        """
        raise NotImplementedError("Subclasses must implement this method.")
