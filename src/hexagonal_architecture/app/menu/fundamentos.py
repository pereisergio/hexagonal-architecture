from hexagonal_architecture.app.fundamentos.dependency_inversion import DIP
from hexagonal_architecture.app.fundamentos.polimorfismo import Polimorfismo
from hexagonal_architecture.app.utils.terminal import TerminalUtils


class MenuFundamentos:
    @staticmethod
    async def menu(stdscr):
        while True:
            TerminalUtils.titulo(stdscr, "Fundamentos")
            idx, option = await TerminalUtils.menu_vertical(
                stdscr,
                [
                    "1. Polimorfismo",
                    "2. Princípio da Inversão de Dependência (DIP)",
                    "3. Voltar",
                ],
            )
            match idx:
                case 0:
                    await Polimorfismo.menu(stdscr)
                case 1:
                    await DIP.menu(stdscr)
                case 2:
                    return
