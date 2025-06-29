from hexagonal_architecture.app.utils.terminal import TerminalUtils
from hexagonal_architecture.core.fundamentos.carro import Carro
from hexagonal_architecture.core.fundamentos.ferrari import Ferrari
from hexagonal_architecture.core.fundamentos.fusca import Fusca


class Polimorfismo:
    @staticmethod
    async def menu(stdscr):
        TerminalUtils.titulo(stdscr, "Polimorfismo")
        idx, _ = TerminalUtils.menu_vertical(
            stdscr, ["1. Ferrari", "2. Fusca", "3. Voltar"]
        )
        match idx:
            case 0:
                TerminalUtils.limpar(stdscr)
                await Polimorfismo.executar(stdscr, Ferrari())
            case 1:
                TerminalUtils.limpar(stdscr)
                await Polimorfismo.executar(stdscr, Fusca())
            case 2:
                return

    @staticmethod
    async def executar(stdscr, carro: Carro):
        ultimo_idx = 0  # Mantém a última opção selecionada
        while True:
            TerminalUtils.titulo(stdscr, f"Polimorfismo - {carro.__class__.__name__}")
            stdscr.addstr(4, 1, f"Velocidade Máxima: {carro.velocidade_maxima} km/h")
            stdscr.addstr(5, 1, f"Velocidade Atual: {carro.velocidade_atual} km/h")
            stdscr.addstr(7, 1, "Escolha uma ação:")
            idx, _ = TerminalUtils.menu_horizontal(
                stdscr, ["Acelerar", "Frear", "Sair"], y_pos=9, idx_inicial=ultimo_idx
            )
            ultimo_idx = idx  # Salva a opção selecionada para a próxima iteração
            match idx:
                case 0:
                    carro.acelerar()
                case 1:
                    carro.frear()
                case 2:
                    return
