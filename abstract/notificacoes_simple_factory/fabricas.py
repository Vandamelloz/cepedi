from classes import Notificacao, NotificarSMS, NotificarEmail, NotificarWhatsapp
from notificacao_factory import NotificacaoFactory
#priorizar whatsapp

class NotificacaoUrgente(NotificacaoFactory):

    def criarEmail(self) -> Notificacao:
        
        return NotificarEmail()
 
    def criarSms(self)-> Notificacao:
        return NotificarSMS()
  
    def criarWhatsapp(self) -> Notificacao:
        print("Urgente")
        return NotificarWhatsapp()

class NotificacaoNormal(NotificacaoFactory):

    def criarEmail(self) -> Notificacao:
        
        return NotificarEmail()
 
    def criarSms(self)-> Notificacao:
        return NotificarSMS()
  
    def criarWhatsapp(self) -> Notificacao:
        print("Normal")
        return NotificarWhatsapp()