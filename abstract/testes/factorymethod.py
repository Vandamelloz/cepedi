from classteste import Animal
from classcao import Cao
from classgato import Gato
from abc import ABC, abstractmethod

class AnimalFactory(ABC):
    @abstractmethod
    def CriarAnimais(self):
      pass
