import curses


class TerminalUtils:
    @staticmethod
    def _get_next_available_line(stdscr) -> int:
        """
        Detecta a próxima linha disponível para escrita, verificando qual foi
        a última linha que contém informação na tela
        """
        height, width = stdscr.getmaxyx()

        # Verifica de baixo para cima qual é a última linha com conteúdo
        for y in range(height - 1, -1, -1):
            line_content = ""
            try:
                # Lê o conteúdo da linha atual
                for x in range(width - 1):
                    char = stdscr.inch(y, x) & 0xFF  # Pega apenas o caractere
                    if char != 32:  # 32 = espaço em ASCII
                        line_content += chr(char)

                # Se encontrou conteúdo não vazio, a próxima linha disponível é y + 1
                if line_content.strip():
                    return min(y + 1, height - 1)  # Garante que não ultrapasse a tela

            except curses.error:
                # Ignora erros ao ler posições inválidas
                continue

        # Se não encontrou nenhuma linha com conteúdo, retorna linha 3 (após título)
        return 0

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
    def exibir_mensagem(stdscr, mensagem: str, cor_pair=5):
        """Exibe uma mensagem na próxima linha disponível"""
        y_pos = TerminalUtils._get_next_available_line(stdscr) + 1
        TerminalUtils.__init_colors()
        stdscr.addstr(y_pos, 1, mensagem, curses.color_pair(cor_pair))
        stdscr.refresh()

    @staticmethod
    def exibir_chave_valor(stdscr, chave: str, valor: str | float):
        """Exibe chave e valor na próxima linha disponível"""
        y_pos = TerminalUtils._get_next_available_line(stdscr) + 1
        TerminalUtils.__init_colors()
        stdscr.addstr(y_pos, 1, chave, curses.color_pair(12))  # Chave em amarelo
        stdscr.addstr(
            y_pos, 1 + len(chave), str(valor), curses.color_pair(2)
        )  # Valor em verde
        stdscr.refresh()

    @staticmethod
    async def menu_vertical(stdscr, options, idx_inicial=0):
        """Menu com opções dispostas verticalmente, posicionado automaticamente"""
        y_pos = TerminalUtils._get_next_available_line(stdscr) + 1
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
    async def menu_horizontal(stdscr, options, idx_inicial=0):
        """Menu com opções dispostas horizontalmente, posicionado automaticamente"""
        y_pos = TerminalUtils._get_next_available_line(stdscr) + 1
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
    async def esperar_enter(stdscr, mensagem="Pressione ENTER para continuar..."):
        """Espera ENTER posicionando automaticamente na próxima linha disponível"""
        y_pos = TerminalUtils._get_next_available_line(stdscr) + 1
        TerminalUtils.__init_colors()
        stdscr.addstr(y_pos, 1, mensagem, curses.color_pair(5))
        stdscr.refresh()

        # Loop até pressionar ENTER
        while True:
            key = stdscr.getch()
            if key in [curses.KEY_ENTER, 10, 13]:  # ENTER pode ser 10 ou 13
                break

    @staticmethod
    async def campo_required(
        stdscr, label: str, valor_padrao: str = "", cor_pair=12
    ) -> str:
        """
        Exibe um campo obrigatório que nunca retorna valor vazio.
        Se não houver entrada, usa valor_padrao (se válido).
        Se valor_padrao for inválido, fica em loop até entrada válida.
        """
        while True:
            y_pos = TerminalUtils._get_next_available_line(stdscr) + 1
            TerminalUtils.__init_colors()

            # Exibe o label
            stdscr.addstr(y_pos, 1, label, curses.color_pair(cor_pair))

            # Exibe o valor padrão se existir e for válido
            if valor_padrao and valor_padrao.strip():
                stdscr.attron(curses.color_pair(13))
                stdscr.addstr(y_pos, len(label) + 2, valor_padrao)
                stdscr.attroff(curses.color_pair(13))

            stdscr.refresh()

            # Ativa o modo de entrada
            curses.echo()
            curses.curs_set(1)

            try:
                # Posiciona o cursor após o label
                stdscr.move(y_pos, len(label) + 2)

                # Implementa captura manual para apagar valor padrão ao digitar
                entrada = ""
                valor_padrao_apagado = False

                while True:
                    key = stdscr.getch()

                    if key in [curses.KEY_ENTER, 10, 13]:  # Enter
                        break
                    elif key in [curses.KEY_BACKSPACE, 127, 8]:  # Backspace
                        if entrada:
                            entrada = entrada[:-1]
                            # Reescreve a linha
                            stdscr.move(y_pos, len(label) + 2)
                            stdscr.clrtoeol()
                            if entrada:
                                stdscr.addstr(
                                    y_pos,
                                    len(label) + 2,
                                    entrada,
                                    curses.color_pair(13),
                                )
                            stdscr.move(y_pos, len(label) + 2 + len(entrada))
                    elif key == 27:  # ESC - cancela e reinicia o campo
                        entrada = ""
                        valor_padrao_apagado = False
                        stdscr.move(y_pos, len(label) + 2)
                        stdscr.clrtoeol()
                        if valor_padrao and valor_padrao.strip():
                            stdscr.addstr(
                                y_pos,
                                len(label) + 2,
                                valor_padrao,
                                curses.color_pair(13),
                            )
                        stdscr.move(y_pos, len(label) + 2)
                    elif 32 <= key <= 126:  # Caracteres imprimíveis
                        # Se é a primeira tecla digitada e há valor padrão, apaga o valor padrão
                        if (
                            not valor_padrao_apagado
                            and valor_padrao
                            and valor_padrao.strip()
                        ):
                            stdscr.move(y_pos, len(label) + 2)
                            stdscr.clrtoeol()  # Apaga o valor padrão
                            valor_padrao_apagado = True

                        # Adiciona o caractere digitado
                        entrada += chr(key)

                        # Reescreve a entrada
                        stdscr.move(y_pos, len(label) + 2)
                        stdscr.addstr(
                            y_pos, len(label) + 2, entrada, curses.color_pair(13)
                        )
                        stdscr.move(y_pos, len(label) + 2 + len(entrada))

                    stdscr.refresh()

                # Se digitou algo válido, retorna
                if entrada.strip():
                    return entrada.strip()

                # Se não digitou nada, verifica se há valor padrão válido
                if valor_padrao and valor_padrao.strip():
                    # Reexibe o valor padrão na tela
                    stdscr.addstr(
                        y_pos, len(label) + 2, valor_padrao, curses.color_pair(13)
                    )
                    stdscr.refresh()
                    return valor_padrao.strip()

                # Se chegou aqui, não há entrada válida nem valor padrão válido
                # Mostra erro e continua o loop
                error_y = y_pos + 1
                height, _ = stdscr.getmaxyx()
                if error_y < height - 1:
                    stdscr.addstr(
                        error_y,
                        1,
                        "Campo obrigatório! Digite um valor válido.",
                        curses.color_pair(3),
                    )
                    stdscr.refresh()
                    curses.napms(1500)  # Pausa por 1.5 segundos
                    # Limpa a mensagem de erro
                    stdscr.move(error_y, 1)
                    stdscr.clrtoeol()
                    stdscr.refresh()

            except curses.error:
                # Se der erro, continua o loop
                pass
            finally:
                curses.noecho()
                curses.curs_set(0)

    @staticmethod
    def __init_colors():
        """Função auxiliar para inicializar todas as cores"""
        curses.start_color()

        curses.init_pair(1, curses.COLOR_BLUE, curses.COLOR_BLACK)
        curses.init_pair(2, curses.COLOR_GREEN, curses.COLOR_BLACK)
        curses.init_pair(3, curses.COLOR_RED, curses.COLOR_BLACK)
        curses.init_pair(4, curses.COLOR_CYAN, curses.COLOR_BLACK)
        curses.init_pair(5, curses.COLOR_WHITE, curses.COLOR_BLACK)
        curses.init_pair(6, curses.COLOR_BLACK, curses.COLOR_WHITE)
        curses.init_pair(7, curses.COLOR_WHITE, curses.COLOR_BLUE)
        curses.init_pair(8, curses.COLOR_YELLOW, curses.COLOR_RED)
        curses.init_pair(9, curses.COLOR_YELLOW, curses.COLOR_WHITE)
        curses.init_pair(11, curses.COLOR_RED, curses.COLOR_WHITE)
        curses.init_pair(10, curses.COLOR_MAGENTA, curses.COLOR_BLACK)
        curses.init_pair(12, curses.COLOR_YELLOW, curses.COLOR_BLACK)
        curses.init_pair(13, curses.COLOR_MAGENTA, curses.COLOR_WHITE)
