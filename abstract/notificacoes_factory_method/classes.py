from abc import ABC, abstractmethod

class Notificacao(ABC):
    @abstractmethod
    def notificar(self):
        pass
    
class NotificarEmail(Notificacao):
    def notificar(self, destinatario, mensagem: str):
       print(f"{destinatario}, recebeu {mensagem} por Email")
class NotificarSMS(Notificacao):
    def notificar(self, destinatario, mensagem: str):
        print(f"{destinatario}, recebeu {mensagem} por SMS")
class NotificarWhatsapp(Notificacao):
    def notificar(self, destinatario, mensagem: str):
        print(f"{destinatario}, recebeu {mensagem} por Whatsapp")