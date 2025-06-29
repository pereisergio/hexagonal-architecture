from abc import ABC, abstractmethod


class Carro(ABC):
    @property
    @abstractmethod
    def velocidade_maxima(self) -> int:
        pass

    @property
    @abstractmethod
    def velocidade_atual(self) -> int:
        pass

    @abstractmethod
    def acelerar(self) -> None:
        pass

    @abstractmethod
    def frear(self) -> None:
        pass
