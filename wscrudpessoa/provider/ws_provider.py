import json
from http.server import HTTPServer, BaseHTTPRequestHandler
from urllib.parse import urlparse, parse_qs
from pessoa_service import PessoaService

# Classe Provider para lidar com as requisições HTTP
class WSProvider(BaseHTTPRequestHandler):

    def do_GET(self):
        #http://127.0.0.1:8000/pessoas
        servico=PessoaService()
        resultado=servico.listarTodas()
        if self.path.startswith("/pessoas"):
            self.send_response(200)
            self.send_header('Content-type', 'application/json')
            self.end_headers()
            lista_pessoa=[]
            for pessoa in resultado:
                lista_pessoa.append({
                "email": pessoa.email,
                "nome": pessoa.nome,
                "idade": pessoa.idade,
                "altura": pessoa.altura
                })

            # msg_retorno = {"resultado": resultado}
            resposta = json.dumps(lista_pessoa).encode('utf-8')
            self.wfile.write(resposta)
        


def main():
    # Inicia o servidor HTTP na porta 8081
    servidor = HTTPServer(('172.12.172.246', 8081), WSProvider)
    print("Servidor iniciado em http:172.12.172.246:8081")
    servidor.serve_forever()

if __name__ == "__main__":
    main()