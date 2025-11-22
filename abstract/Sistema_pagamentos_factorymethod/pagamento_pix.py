from pagamentofactory import pagamentoFactory
from pagamentoPixclass import Pix

class PagarPix(pagamentoFactory):
    def BuscarPagamento(self):
        return Pix()