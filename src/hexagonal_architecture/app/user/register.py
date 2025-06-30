from hexagonal_architecture.app.utils.terminal import TerminalUtils
from hexagonal_architecture.core.user.models.user import ConcreteUser
from hexagonal_architecture.core.user.services.register import UserRegister


class Register:
    @staticmethod
    async def execute(stdscr):
        TerminalUtils.titulo(stdscr, "Registrar Usuário")

        user_id = await TerminalUtils.campo_required(stdscr, "Id: ", "5546548")
        name = await TerminalUtils.campo_required(stdscr, "Nome: ", "João da Silva")
        email = await TerminalUtils.campo_required(stdscr, "Email: ", "joao@email.com")
        senha = await TerminalUtils.campo_required(stdscr, "Senha: ", "senha123")

        usuario = ConcreteUser(user_id=user_id, name=name, email=email, password=senha)
        await UserRegister().execute(user=usuario)
        TerminalUtils.exibir_mensagem(stdscr, "Usuário registrado com sucesso!", 2)
        await TerminalUtils.esperar_enter(stdscr)
