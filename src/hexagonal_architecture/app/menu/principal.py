from hexagonal_architecture.app.menu.fundamentals import MenuFundamentos
from hexagonal_architecture.app.utils.terminal import TerminalUtils


class MenuPrincipal:
    @staticmethod
    async def menu(stdscr):
        while True:
            TerminalUtils.titulo(stdscr, "Menu Principal", 5)
            idx, option = await TerminalUtils.menu_vertical(
                stdscr, ["1. Fundamentos", "2. Sair"]
            )
            match idx:
                case 0:
                    await MenuFundamentos.menu(stdscr)
                case 1:
                    return
