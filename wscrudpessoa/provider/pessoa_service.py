from pessoa import Pessoa

class PessoaService:
    
    def __init__(self):
        self._pessoas=[
            Pessoa(email="joao@gmail.com", nome="Joãozin",idade=12,altura=1.40),
            Pessoa(email="veganinha@vegie.vegan.com", nome="Vegana",idade=24,altura=1.77),
            Pessoa(email="yan@gmail.com", nome="Yan",idade=27,altura=1.73)
        ]

    def listarTodas(self) -> list:
       return self._pessoas