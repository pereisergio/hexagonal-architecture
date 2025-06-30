from hexagonal_architecture.app.utils.terminal import TerminalUtils
from hexagonal_architecture.core.fundamentals.carro import Carro
from hexagonal_architecture.core.fundamentals.civic import Civic
from hexagonal_architecture.core.fundamentals.ferrari import Ferrari
from hexagonal_architecture.core.fundamentals.fusca import Fusca


class Polimorfismo:
    @staticmethod
    async def menu(stdscr):
        TerminalUtils.titulo(stdscr, "Polimorfismo")
        idx, _ = await TerminalUtils.menu_vertical(
            stdscr, ["1. Ferrari", "2. Fusca", "3. Civic", "Voltar"]
        )
        match idx:
            case 0:
                TerminalUtils.limpar(stdscr)
                await Polimorfismo.executar(stdscr, Ferrari())
            case 1:
                TerminalUtils.limpar(stdscr)
                await Polimorfismo.executar(stdscr, Fusca())
            case 2:
                TerminalUtils.limpar(stdscr)
                await Polimorfismo.executar(stdscr, Civic())
            case _:
                return

    @staticmethod
    async def executar(stdscr, carro: Carro):
        ultimo_idx = 0  # Mantém a última opção selecionada
        while True:
            TerminalUtils.titulo(stdscr, f"Polimorfismo - {carro.__class__.__name__}")
            TerminalUtils.exibir_chave_valor(
                stdscr, "Velocidade Máxima: ", f"{carro.velocidade_maxima} km/h"
            )
            TerminalUtils.exibir_chave_valor(
                stdscr, "Velocidade Atual: ", f"{carro.velocidade_atual} km/h"
            )
            TerminalUtils.exibir_mensagem(stdscr, "Escolha uma ação:")
            idx, _ = await TerminalUtils.menu_horizontal(
                stdscr, ["Acelerar", "Frear", "Sair"], idx_inicial=ultimo_idx
            )
            ultimo_idx = idx  # Salva a opção selecionada para a próxima iteração
            match idx:
                case 0:
                    carro.acelerar()
                case 1:
                    carro.frear()
                case _:
                    return
