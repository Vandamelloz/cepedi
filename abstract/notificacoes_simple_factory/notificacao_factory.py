from abc import ABC, abstractmethod
from classes import Notificacao

class NotificacaoFactory(ABC):
    @abstractmethod
    def criarEmail(self, destinatario, mensagem: str) -> Notificacao:
        pass
    @abstractmethod
    def criarSms(self, destinatario, mensagem:str)-> Notificacao:
        pass
    @abstractmethod
    def criarWhatsapp(self, destinatario, mensagem:str) -> Notificacao:
        pass
