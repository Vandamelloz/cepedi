from classes import Notificacao, NotificarSMS, NotificarEmail, NotificarWhatsapp
from notificacao_factory import NotificacaoFactory
#priorizar whatsapp

class NotificacaoUrgente(NotificacaoFactory):

    def criarEmail(self) -> Notificacao:
        
        return NotificarEmail()
 
    def criarSms(self) -> Notificacao:
        return NotificarSMS()
  
    def criarWhatsapp(self) -> Notificacao:
        print("Ordem de prioridade: Urgente")
        return NotificarWhatsapp()

class NotificacaoNormal(NotificacaoFactory):

    def criarEmail(self) -> Notificacao:
        
        return NotificarEmail()
 
    def criarSms(self) -> Notificacao:
        print("Ordem de prioridade: Normal")
        return NotificarSMS()
  
    def criarWhatsapp(self) -> Notificacao:
        return NotificarWhatsapp()

class NotificacaoTrabalho(NotificacaoFactory):

    def criarEmail(self) -> Notificacao:
        print("Ordem de prioridade: Trabalho")
        return NotificarEmail()
 
    def criarSms(self) -> Notificacao:
        return NotificarSMS()
  
    def criarWhatsapp(self) -> Notificacao:
        return NotificarWhatsapp()