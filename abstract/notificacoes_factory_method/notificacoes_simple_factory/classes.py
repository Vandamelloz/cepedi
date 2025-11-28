from abc import ABC, abstractmethod


class Notificacao(ABC):
    @abstractmethod
    def notificar(self, destinatario: str, mensagem: str):
        pass

class NotificarEmail(Notificacao):
    def notificar(self, destinatario: str, mensagem: str):
        print(f"[EMAIL] Notificação enviada para {destinatario}: '{mensagem}'")

class NotificarSMS(Notificacao):
    def notificar(self, destinatario: str, mensagem: str):
        print(f"[SMS] Notificação enviada para {destinatario}: '{mensagem}'")

class NotificarWhatsapp(Notificacao):
    def notificar(self, destinatario: str, mensagem: str):
        print(f"[WHATSAPP] Notificação enviada para {destinatario}: '{mensagem}'")