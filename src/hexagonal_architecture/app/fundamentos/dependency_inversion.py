from hexagonal_architecture.app.utils.terminal import TerminalUtils
from hexagonal_architecture.core.fundamentos.corrida import corrida


class DIP:
    @staticmethod
    async def menu(stdscr):
        TerminalUtils.titulo(stdscr, "Princípio da Inversão de Dependência (DIP)")
        TerminalUtils.limpar(stdscr)
        corrida(stdscr)
        TerminalUtils.esperar_enter(stdscr, 22, 'Pressione "ENTER" para voltar...')
