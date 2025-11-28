from simple_factory import NotificacaoSimpleFactory

def servico_notificacao(prioridade: str, destinatario: str, mensagem: str):
 

    try:
        notificacao = NotificacaoSimpleFactory.cria_notificacao_por_prioridade(prioridade)
    
        notificacao.notificar(destinatario, mensagem)
        
    except Exception as e:
        print(f"ERRO: Não foi possível criar a notificação. Detalhes: {e}")
    


if __name__ == "__main__":
    
    destinatario_email = "gerente@empresa.com"
    destinatario_celular = "99999-1234"
    mensagem_alerta = "Sistema fora do ar, verificar urgentemente!"
    mensagem_lembrete = "Relatório semanal disponível para visualização."


    servico_notificacao("URGENTE", destinatario_celular, mensagem_alerta)

    servico_notificacao("TRABALHO", destinatario_email, mensagem_lembrete)


    servico_notificacao("NORMAL", destinatario_celular, "Confirmação de pedido: #9876.")