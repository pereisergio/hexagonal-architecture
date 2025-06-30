from .carro import Carro


class Civic(Carro):
    def __init__(self):
        self._velocidade_maxima = 208
        self._velocidade_atual: int = 0

    @property
    def velocidade_maxima(self) -> int:
        return self._velocidade_maxima

    @property
    def velocidade_atual(self) -> int:
        return self._velocidade_atual

    def acelerar(self) -> None:
        self._velocidade_atual = min(
            self._velocidade_atual + 10, self._velocidade_maxima
        )

    def frear(self) -> None:
        self._velocidade_atual = max(self._velocidade_atual - 10, 0)
