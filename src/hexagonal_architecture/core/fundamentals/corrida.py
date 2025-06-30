from hexagonal_architecture.core.fundamentals.carro import Carro
from hexagonal_architecture.utils.output_interface import OutputInterface


def corrida(carro: Carro, output: OutputInterface):
    array = range(0, 10)
    for _ in array:
        carro.acelerar()
        output.write(f"Velocidade: {carro.velocidade_atual} km/h")

    for _ in array:
        carro.frear()
        output.write(f"Velocidade: {carro.velocidade_atual} km/h")
