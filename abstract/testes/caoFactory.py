from factorymethod import AnimalFactory
from classcao import Cao
class CaoFactory(AnimalFactory):
    def criarAnimal(self):
        return Cao()
