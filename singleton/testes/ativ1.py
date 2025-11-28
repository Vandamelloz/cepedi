class AuthManagerSingleton(type):
    _instance = None

    def __call__(self, *args, **kwargs):
        if self._instance is None:
            self._instance = super().__call__(*args, **kwargs)
        return self._instance


class GerenciamentoAutenticacao(metaclass=AuthManagerSingleton):

    def __init__(self, usuario, senha):
        self.usuario = usuario
        self.senha = senha

    def set_usuario(self, usuario):
        self.usuario = usuario

    def set_senha(self, senha):
        self.senha = senha


if __name__ == "__main__":
    usuario = input("Digite o nome do usuário: ")
    senha = input("Digite sua senha: ")

    auth1 = GerenciamentoAutenticacao(usuario, senha)
    auth2 = GerenciamentoAutenticacao("OUTRO", "123")

    


    print(auth1.usuario, auth1.senha)
    print(auth2.usuario, auth2.senha)

    print(auth1 is auth2)  # Deve dar True -> singleton
