from classes import Notificacao, NotificarSMS, NotificarEmail, NotificarWhatsapp
from fabricas import NotificacaoUrgente, NotificacaoNormal, NotificacaoTrabalho 

if __name__=="__main__":

    mensagem = input("Digite aqui sua mensagem: ")
    destinatario = input("Digite o nome do destinátario: ")
    
    escolha = input("Digite a opção de mensagem(1-SMS/2-Whatsapp/3-Email): ")

    try:
        escolha = int(escolha)
    except ValueError:
        print("Erro: A opção deve ser um número inteiro (1, 2 ou 3).")
        exit()
        
    
    match escolha:
        case 1:
            fabrica = NotificacaoNormal()
            fabrica.criarSms().notificar(destinatario, mensagem)

        case 2:
            fabrica = NotificacaoUrgente()
            fabrica.criarWhatsapp().notificar(destinatario, mensagem) 
        case 3:
            fabrica = NotificacaoTrabalho()
            fabrica.criarEmail().notificar(destinatario, mensagem) 
        case _:
            print("Escolha inválida! Por favor, digite 1, 2 ou 3.")




    '''
    sms=Not()
    destinatario=input("Digite o destinatário de sua mensagem: ")
    mensagem=input("Digite a mensagem que ele deve receber: ")
    sms.criarSms().notificar(destinatario, mensagem)
    whatsapp= Not()
    whatsapp.criarWhatsapp().notificar(destinatario, mensagem)'''
