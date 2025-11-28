from classes import Notificacao, NotificarSMS, NotificarEmail, NotificarWhatsapp
from fabricas import NotificacaoUrgente, NotificacaoNormal

if __name__=="__main__":

    email= NotificacaoUrgente()
    email.criarWhatsapp().notificar("rick", "OI")
    
    whats = NotificacaoNormal()
    whats.criarWhatsapp().notificar("Vanda", "OI")


    '''
    sms=Not()
    destinatario=input("Digite o destinatário de sua mensagem: ")
    mensagem=input("Digite a mensagem que ele deve receber: ")
    sms.criarSms().notificar(destinatario, mensagem)
    whatsapp= Not()
    whatsapp.criarWhatsapp().notificar(destinatario, mensagem)'''
