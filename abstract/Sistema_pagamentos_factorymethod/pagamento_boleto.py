from pagamentofactory import pagamentoFactory
from pagamentoBoletoclass import Boleto

class PagarBoleto(pagamentoFactory):
    @staticmethod
    def BuscarPagamento():
        return Boleto()