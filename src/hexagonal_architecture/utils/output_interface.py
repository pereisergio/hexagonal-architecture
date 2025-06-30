import curses
from typing import Protocol


class OutputInterface(Protocol):
    """Interface para diferentes tipos de saída (print, log, curses, etc.)"""

    def write(self, message: str) -> None:
        """Escreve uma mensagem na próxima linha disponível"""
        ...


class PrintOutput:
    """Implementação usando print para saída no console"""

    @staticmethod
    def write(message: str) -> None:
        print(message)


class LogOutput:
    """Implementação usando log para saída em arquivo"""

    def __init__(self, logger):
        self.logger = logger

    def write(self, message: str) -> None:
        self.logger.info(message)


class CursesOutput:
    """Implementação usando curses para saída na tela"""

    def __init__(self, stdscr):
        self.stdscr = stdscr
        # Detecta onde começar baseado no conteúdo atual
        self.next_available_line = self._get_next_available_line(self.stdscr) + 1

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

    def write(self, message: str) -> None:
        y_pos = CursesOutput._get_next_available_line(self.stdscr)
        self.stdscr.addstr(y_pos, 1, message)
        self.stdscr.refresh()
