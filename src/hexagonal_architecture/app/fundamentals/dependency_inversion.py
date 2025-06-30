from hexagonal_architecture.app.utils.terminal import TerminalUtils
from hexagonal_architecture.core.fundamentals.civic import Civic
from hexagonal_architecture.core.fundamentals.corrida import corrida
from hexagonal_architecture.core.fundamentals.ferrari import Ferrari
from hexagonal_architecture.core.fundamentals.fusca import Fusca
from hexagonal_architecture.utils.output_interface import CursesOutput


class DIP:
    @staticmethod
    async def menu(stdscr):
        TerminalUtils.titulo(stdscr, "Princípio da Inversão de Dependência (DIP)")
        idx, _ = await TerminalUtils.menu_horizontal(
            stdscr, ["1. Ferrari", "2. Fusca", "3. Civic", "Voltar"]
        )
        match idx:
            case 0:
                carro = Ferrari()
            case 1:
                carro = Fusca()
            case 2:
                carro = Civic()
            case _:
                return

        TerminalUtils.limpar(stdscr)
        curses_output = CursesOutput(stdscr)
        TerminalUtils.titulo(stdscr, f"Corrida com DIP - {carro.__class__.__name__}")
        corrida(carro, curses_output)
        await TerminalUtils.esperar_enter(stdscr, "Pressione ENTER para voltar...")
