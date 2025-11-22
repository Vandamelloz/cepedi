from pagamentoClass import Pagamento

class Boleto(Pagamento):
    def realizarPagamento(self):
        print("Pagamento realizado por boleto!")