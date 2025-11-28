from pagamento_boleto import PagarBoleto
from pagamento_pix import PagarPix
from pagamento_cartao import PagarCartao

if __name__=="__main__":
    pix=PagarPix()
    pagamento1=pix.BuscarPagamento()
    pagamento1.realizarPagamento()

    boleto=PagarBoleto()
    pagamento2=boleto.BuscarPagamento()
    pagamento2.realizarPagamento()
    