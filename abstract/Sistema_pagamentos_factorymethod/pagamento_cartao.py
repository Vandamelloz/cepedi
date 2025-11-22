from pagamentofactory import pagamentoFactory
from pagamentoClass import Pagamento
from pagamentoCartaoclass import Cartao

class PagarCartao(pagamentoFactory):
    @staticmethod
    def BuscarPagamento():
        return Cartao()