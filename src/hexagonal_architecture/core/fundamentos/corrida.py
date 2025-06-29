from hexagonal_architecture.core.fundamentos.fusca import Fusca


def corrida(stdscr):
    carro = Fusca()
    array = range(0, 10)
    count = 1
    for _ in array:
        carro.acelerar()
        stdscr.addstr(count, 1, f"Velocidade: {carro.velocidade_atual} km/h")
        count += 1

    for _ in array:
        carro.frear()
        stdscr.addstr(count, 1, f"Velocidade: {carro.velocidade_atual} km/h")
        count += 1
