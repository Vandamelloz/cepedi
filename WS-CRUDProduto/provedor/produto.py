class Produto:
    def __init__(self, codigo: str, nome: str, preco: float, quantidade: int):
        self.__codigo = codigo
        self.__nome = nome
        self.__preco = preco
        self.__quantidade = quantidade

    @property
    def codigo(self,):
        return self.__codigo
    
    @property
    def nome(self,):
        return self.__nome

    @nome.setter
    def nome(self, value):
        self.__nome = value
    
    @property
    def preco(self,):
        return self.__preco

    @preco.setter
    def preco(self, value):
        try:
            self.__preco = float(value)
        except Exception:
            self.__preco = 0.0
    
    @property
    def quantidade(self,):
        return self.__quantidade

    @quantidade.setter
    def quantidade(self, value):
        try:
            self.__quantidade = int(value)
        except Exception:
            self.__quantidade = 0