from classes import Notificacao, NotificarEmail, NotificarSMS, NotificarWhatsapp

class NotificacaoSimpleFactory:

    @staticmethod
    def cria_notificacao_por_prioridade(prioridade: str) -> Notificacao:
     
        
        prioridade = prioridade.lower()
        
        if prioridade == "urgente":
        
            print(f"[Fábrica] Prioridade: {prioridade.upper()}. Criando Notificação WHATSAPP...")
            return NotificarWhatsapp()
        
        elif prioridade == "trabalho":
          
            print(f"[Fábrica] Prioridade: {prioridade.upper()}. Criando Notificação EMAIL...")
            return NotificarEmail()
        
        elif prioridade == "normal":
            
            print(f"[Fábrica] Prioridade: {prioridade.upper()}. Criando Notificação SMS...")
            return NotificarSMS()
        
        else:
        
            print(f"[Fábrica] Prioridade desconhecida ({prioridade}). Criando Notificação EMAIL (Padrão)...")
            return NotificarEmail()