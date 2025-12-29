import requests

from provedor.produto import Produto

class ProdutoCliente:
    def __init__(self):
        # usa 127.0.0.1 para evitar problemas de resolução IPv4/IPv6 no Windows
        self.base_url = "http://127.0.0.1:8080"
    
    def listarTodos(self,):
        print("VOU LISTAR TODOS")
        endpoint_listar = f"{self.base_url}/produto/listar"

        try:
            response = requests.get(endpoint_listar, timeout=5)
            response.raise_for_status()
        except requests.RequestException as e:
            print(f"Erro! --> {e}")
            return

        try:
            resposta = response.json()
        except ValueError:
            print("Resposta não é JSON")
            return

        print("="*30)
        for i in resposta:
            print(f"Codigo: {i['codigo']}\n"
                  f"Nome: {i['nome']}\n"
                  f"Preço: {i['preco']}\n"
                  f"Quantidade: {i['quantidade']}")
            print("="*30)
    
    def buscarPorCodigo(self, param: str):
        print("VOU BUSCAR POR CÓDIGO")
        endpoint_buscar = f"{self.base_url}/produto/buscar"

        dados = f"?codigo={param}"

        try:
            response = requests.get(url= endpoint_buscar + dados, timeout=5)
            response.raise_for_status()
        except requests.RequestException as e:
            print(f"Erro! --> {e}")
            return

        try:
            i = response.json()
        except ValueError:
            print("Resposta não é JSON")
            return

        if response.status_code == 200:
            print("="*30)
            print(f"Codigo: {i['codigo']}\n"
                  f"Nome: {i['nome']}\n"
                  f"Preço: {i['preco']}\n"
                  f"Quantidade: {i['quantidade']}")
            print("="*30)
        else:
            print("="*30)
            print(i.get('erro', 'Erro desconhecido'))
            print("="*30)
    
    def adicionarProdutos(self, produto: Produto):
        endpoint_criar = f"{self.base_url}/produto/criar"

        print("VOU TENTAR ADICIONAR O PRODUTO")
        dados = {
            "codigo": produto.codigo,
            "nome": produto.nome,
            "preco": produto.preco,
            "quantidade": produto.quantidade
        }

        try:
            response = requests.post(endpoint_criar, data=dados, timeout=5)
            response.raise_for_status()
        except requests.RequestException as e:
            print(f"Erro! --> {e}")
            return

        try:
            r = response.json()
        except ValueError:
            print("Resposta não é JSON")
            return

        if response.status_code in (200, 201):
            print(r.get('sucesso', 'Produto adicionado'))
        else:
            print(r.get('erro', 'Erro desconhecido'))
    
    def deletarProduto(self, param):
        print("VOU APAGAR ITEM")
        endpoint_deletar = f"{self.base_url}/produto/deletar"

        dados = {"codigo": param}

        try:
            response = requests.post(endpoint_deletar, data=dados, timeout=5)
            response.raise_for_status()
        except requests.RequestException as e:
            print(f"Erro! --> {e}")
            return

        try:
            r = response.json()
        except ValueError:
            print("Resposta não é um JSON")
            return
        
        if response.status_code in (200, 201):
            print(r.get('sucesso', 'Produto adicionado'))
        else:
            print(r.get('erro', 'Erro desconhecido'))
    
    def atualizarProduto(self, produto: Produto):
        print("VOU ATUALIZAR PRODUTO")
        endpoint_atualizar = f"{self.base_url}/produto/atualizar"

        dados = {
            "codigo": produto.codigo,
            "nome": produto.nome,
            "preco": produto.preco,
            "quantidade": produto.quantidade
        }

        try:
            response = requests.post(endpoint_atualizar, data=dados, timeout=5)
            response.raise_for_status()
        except requests.RequestException as e:
            print(f"Erro! --> {e}")
            return

        try:
            r = response.json()
        except ValueError:
            print("Resposta não é JSON")
            return

        if response.status_code in (200, 201):
            print(r.get('sucesso', 'Produto atualizado'))
        else:
            print(r.get('erro', 'Erro desconhecido'))