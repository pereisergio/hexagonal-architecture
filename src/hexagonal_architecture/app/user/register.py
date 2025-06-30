from hexagonal_architecture.app.utils.terminal import TerminalUtils


class Register:
    @staticmethod
    async def execute(stdscr):
        TerminalUtils.titulo(stdscr, "Registrar Usuário")

        await TerminalUtils.esperar_enter(stdscr)
