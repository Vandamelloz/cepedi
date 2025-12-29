from produto import Produto

class ProdutoService:

    def __init__(self,):
        self.__produtos = [
            Produto(codigo= "116273", nome= "Blusa", preco= 35.75, quantidade= 12),
            Produto(codigo= "115527", nome= "Calça", preco= 65.99, quantidade= 18),
        ]
    
    #Listar todos os produtos
    def listarTodos(self,) -> list:
        return self.__produtos
    
    #Lista apenas produto encontrado
    def buscarPorCodigo(self, param):
        for i in self.__produtos:
            if param == i.codigo:
                return i
        return None
    
    def adicionarProduto(self, produto: Produto):
        if produto is not None:
            print(f"{produto.nome} adicionado")
            self.__produtos.append(produto)
            #return True
        else:
            print("Não é possível adicionar produto")
            #return False
    
    def atualizarProduto(self, produto: Produto):
        """Atualiza um produto existente. Retorna True se encontrado e atualizado, False caso contrário."""
        if produto is None:
            return False

        for i in self.__produtos:
            if produto.codigo == i.codigo:
                # normaliza tipos recebidos como string
                try:
                    preco_v = float(produto.preco) if isinstance(produto.preco, str) else produto.preco
                except Exception:
                    preco_v = 0.0
                try:
                    quantidade_v = int(produto.quantidade) if isinstance(produto.quantidade, str) else produto.quantidade
                except Exception:
                    quantidade_v = 0

                i.nome = produto.nome
                i.preco = preco_v
                i.quantidade = quantidade_v
                print(f"Produto {produto.codigo} atualizado")
                return True

        # não encontrou o produto
        return False

    def deletarProduto(self, param):
        for i in self.__produtos:
            if param == i.codigo:
                self.__produtos.remove(i)