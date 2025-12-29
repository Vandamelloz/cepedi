import requests

class PessoaCliente:
    def __init__(self):
        self.base_url = "http://172.12.172.246:8081"

    def listar_pessoas(self):
       
        endpoint_pessoas = f"{self.base_url}/pessoas"

        #print(f"Consultando:{endpoint_pessoas}...")
        
        response= requests.get(endpoint_pessoas)

        dados_json = response.json()
        for pessoa in dados_json:
            print(f"EMAIL: {pessoa['email']}, NOME:{pessoa['nome']}, IDADE:{pessoa['idade']}, ALTURA:{pessoa['altura']}")


if __name__ == "__main__":
    cliente = PessoaCliente()
    cliente.listar_pessoas()