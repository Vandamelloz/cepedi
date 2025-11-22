from abc import ABC, abstractmethod

class Pagamento(ABC):
    @abstractmethod
    def realizarPagamento(self):
        pass