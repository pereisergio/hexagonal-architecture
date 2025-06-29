import curses


class TerminalUtils:
    @staticmethod
    def titulo(stdscr, titulo, cor_pair=5):
        stdscr.clear()
        TerminalUtils.desenhar_titulo(stdscr, titulo, cor_pair)

    @staticmethod
    def desenhar_titulo(stdscr, titulo, cor_pair=5):
        TerminalUtils.__init_colors()
        stdscr.addstr(1, 1, titulo, curses.color_pair(cor_pair) | curses.A_BOLD)
        stdscr.addstr(2, 1, "─" * len(titulo), curses.color_pair(10))

    @staticmethod
    def limpar(stdscr):
        stdscr.clear()

    @staticmethod
    def menu_vertical(stdscr, options, y_pos=4, idx_inicial=0):
        """Menu com opções dispostas verticalmente (uma embaixo da outra)"""
        curses.curs_set(0)
        TerminalUtils.__init_colors()
        idx = idx_inicial  # Inicia com o índice especificado

        while True:
            # Exibe opções verticalmente
            for i, opcao in enumerate(options):
                if i == idx:
                    stdscr.attron(curses.A_REVERSE)
                    stdscr.addstr(i + y_pos, 2, opcao)
                    stdscr.attroff(curses.A_REVERSE)
                else:
                    stdscr.addstr(i + y_pos, 2, opcao)

            stdscr.refresh()
            key = stdscr.getch()

            if key == curses.KEY_UP and idx > 0:
                idx -= 1
            elif key == curses.KEY_DOWN and idx < len(options) - 1:
                idx += 1
            elif key in [curses.KEY_ENTER, 10, 13]:
                return idx, options[idx]

    @staticmethod
    def menu_horizontal(stdscr, options, y_pos=3, idx_inicial=0):
        """Menu com opções dispostas horizontalmente (uma do lado da outra)"""
        curses.curs_set(0)
        TerminalUtils.__init_colors()
        idx = idx_inicial  # Inicia com o índice especificado

        while True:
            # Exibe opções horizontalmente
            x_pos = 2
            for i, opcao in enumerate(options):
                if i == idx:
                    stdscr.attron(curses.A_REVERSE)
                    stdscr.addstr(y_pos, x_pos, f" {opcao} ", curses.color_pair(11))
                    stdscr.attroff(curses.A_REVERSE)
                else:
                    stdscr.addstr(y_pos, x_pos, f" {opcao} ")

                # Calcula próxima posição X (largura da opção + espaços)
                x_pos += len(opcao) + 4

            stdscr.refresh()
            key = stdscr.getch()

            if key == curses.KEY_LEFT and idx > 0:
                idx -= 1
            elif key == curses.KEY_RIGHT and idx < len(options) - 1:
                idx += 1
            elif key in [curses.KEY_ENTER, 10, 13]:
                return idx, options[idx]

    @staticmethod
    def __init_colors():
        """Função auxiliar para inicializar todas as cores"""
        curses.start_color()
        # Texto colorido com fundo preto
        curses.init_pair(1, curses.COLOR_BLUE, curses.COLOR_BLACK)
        curses.init_pair(2, curses.COLOR_GREEN, curses.COLOR_BLACK)
        curses.init_pair(3, curses.COLOR_RED, curses.COLOR_BLACK)
        curses.init_pair(4, curses.COLOR_CYAN, curses.COLOR_BLACK)
        curses.init_pair(5, curses.COLOR_WHITE, curses.COLOR_BLACK)
        curses.init_pair(10, curses.COLOR_MAGENTA, curses.COLOR_BLACK)

        # Texto com fundos coloridos
        curses.init_pair(6, curses.COLOR_BLACK, curses.COLOR_WHITE)
        curses.init_pair(7, curses.COLOR_WHITE, curses.COLOR_BLUE)
        curses.init_pair(8, curses.COLOR_YELLOW, curses.COLOR_RED)
        curses.init_pair(9, curses.COLOR_YELLOW, curses.COLOR_WHITE)
        curses.init_pair(11, curses.COLOR_RED, curses.COLOR_WHITE)
