import asyncio
import curses

from hexagonal_architecture.app.menu.principal import MenuPrincipal


async def async_wrapper(stdscr):
    """Wrapper assíncrono para a função menu_principal"""
    await MenuPrincipal.menu(stdscr)


def main():
    def curses_main(stdscr):
        """Função que roda o loop assíncrono dentro do curses"""
        asyncio.run(async_wrapper(stdscr))

    curses.wrapper(curses_main)


if __name__ == "__main__":
    main()
