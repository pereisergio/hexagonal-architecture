from hexagonal_architecture.app.menu.fundamentals import FundamentalsMenu
from hexagonal_architecture.app.menu.user import UserMenu
from hexagonal_architecture.app.utils.terminal import TerminalUtils


class MainMenu:
    @staticmethod
    async def menu(stdscr):
        while True:
            TerminalUtils.titulo(stdscr, "Menu Principal", 5)
            idx, option = await TerminalUtils.menu_vertical(
                stdscr, ["1. Fundamentos", "2. Usuário", "Sair"]
            )
            match idx:
                case 0:
                    await FundamentalsMenu.menu(stdscr)
                case 1:
                    await UserMenu.menu(stdscr)
                case _:
                    return
