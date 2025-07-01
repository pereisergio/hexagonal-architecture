from hexagonal_architecture.adapters.auth.space_password import SpacePassword
from hexagonal_architecture.app.utils.terminal import TerminalUtils
from hexagonal_architecture.core.user.models.user import ConcreteUser
from hexagonal_architecture.core.user.services.register import UserRegister


class Register:
    @staticmethod
    async def execute(stdscr):
        # cripto_provider = ReversePassword()
        cripto_provider = SpacePassword()
        use_case = UserRegister(cripto_provider)

        TerminalUtils.titulo(stdscr, "Registrar Usuário")

        name = await TerminalUtils.campo_required(stdscr, "Nome: ", "João da Silva")
        email = await TerminalUtils.campo_required(stdscr, "Email: ", "joao@email.com")
        senha = await TerminalUtils.campo_required(stdscr, "Senha: ", "senha123")

        usuario = ConcreteUser(name=name, email=email, password=senha)
        try:
            await use_case.execute(user=usuario)
            TerminalUtils.exibir_sucesso(stdscr, "Usuário registrado com sucesso!", 2)
        except ValueError as e:
            TerminalUtils.exibir_erro(stdscr, str(e))
        finally:
            TerminalUtils.exibir_mensagem(stdscr, str(usuario))
            await TerminalUtils.esperar_enter(stdscr)

        try:
            await use_case.execute(user=usuario)
            TerminalUtils.exibir_sucesso(stdscr, "Usuário registrado com sucesso!", 2)
        except ValueError as e:
            TerminalUtils.exibir_erro(stdscr, str(e))
        finally:
            TerminalUtils.exibir_mensagem(stdscr, str(usuario))
            await TerminalUtils.esperar_enter(stdscr)

        return
