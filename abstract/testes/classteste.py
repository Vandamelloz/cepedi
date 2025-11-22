from abc import ABC, abstractmethod
#Simple factory

class Animal(ABC):
    @abstractmethod
    def fazSom(self):
        pass
# a= Animal()
# a.fazSom()
