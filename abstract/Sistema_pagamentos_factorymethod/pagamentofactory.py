from abc import ABC, abstractmethod

class pagamentoFactory(ABC):
    @abstractmethod
    def BuscarPagamento(self):
        pass