from factorymethod import AnimalFactory
from classgato import Gato
class GatoFactory(AnimalFactory):
    @staticmethod
    def criarAnimal():
        return Gato()