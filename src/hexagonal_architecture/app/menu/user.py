from hexagonal_architecture.app.user.register import Register
from hexagonal_architecture.app.utils.terminal import TerminalUtils


class UserMenu:
    @staticmethod
    async def menu(stdscr):
        while True:
            TerminalUtils.titulo(stdscr, "Usuário")
            idx, option = await TerminalUtils.menu_vertical(
                stdscr,
                [
                    "1. Registrar Usuário",
                    "Voltar",
                ],
            )
            match idx:
                case 0:
                    await Register.execute(stdscr)
                case _:
                    return
