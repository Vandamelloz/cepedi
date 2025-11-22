from classteste import Animal
from classcao import Cao
from classgato import Gato

class SimpleFactory:
    @staticmethod
    def CriarAnimais(type:str):
        if type== "cao":
            return Cao()
        elif type=="gato":
            return Gato()
        else:
            raise ValueError("Tipo de animal não encontrado")
