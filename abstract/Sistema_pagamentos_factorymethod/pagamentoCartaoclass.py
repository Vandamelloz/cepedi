from pagamentoClass import Pagamento

class Cartao(Pagamento):
    def realizarPagamento(self):
        print("Pagamento relizado com cartão!")