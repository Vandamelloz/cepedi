import json

from http.server import HTTPServer, BaseHTTPRequestHandler
from urllib.parse import urlparse, parse_qs

from produto import Produto
from produto_service import ProdutoService

# Instância única de serviço para persistir produtos durante a execução do servidor
servico = ProdutoService()

class Provider(BaseHTTPRequestHandler):
    def do_GET(self,):
        print("CHEGUEI AQUI")
        #obtém os paâmetros da requisição GET
        chaminho_passado = urlparse(self.path)

        consultar_param = parse_qs(chaminho_passado.query)
        #só para visualizar itens
        print(consultar_param)

        if self.path.startswith("/produto/listar"):
            print("Listar itens chamado")
            resultado = servico.listarTodos()

            self.lista_produtos = []

            if resultado is not None:
                for i in resultado:
                    self.lista_produtos.append({
                        "codigo": i.codigo,
                        "nome": i.nome,
                        "preco": i.preco,
                        "quantidade": i.quantidade
                    })
                self.send_response(200)
                self.send_header("Content-type", "application/json")
                self.end_headers()
                resposta = json.dumps(self.lista_produtos).encode("utf-8")
                self.wfile.write(resposta)
            else:
                self.send_response(404)
                self.send_header("Content-type", "application/json")
                self.end_headers()
                resposta = json.dumps({"erro": "Produtos não encontrados"}).encode("utf-8")
                self.wfile.write(resposta)

        elif self.path.startswith("/produto/buscar"):
            if "codigo" in consultar_param:
                param = consultar_param["codigo"][0]
                print("RECEBI PARAMETROS")
                resultado = servico.buscarPorCodigo(param)

                if resultado is not None:
                    protudo_dicionario = {
                        "codigo": resultado.codigo,
                        "nome": resultado.nome,
                        "preco": resultado.preco,
                        "quantidade": resultado.quantidade
                    }
                    self.send_response(200)
                    self.send_header("Content-type", "application/json")
                    self.end_headers()
                    resposta = json.dumps(protudo_dicionario).encode("utf-8")
                    self.wfile.write(resposta)
                else:
                    self.send_response(404)
                    self.send_header("Content-type", "application/json")
                    self.end_headers()
                    resposta = json.dumps({"erro": "Produtos não encontrados"}).encode("utf-8")
                    self.wfile.write(resposta)
            else:
                # caminho não reconhecido
                self.send_response(404)
                self.send_header("Content-type", "application/json")
                self.end_headers()
                resposta = json.dumps({"erro": "Caminho não encontrado"}).encode("utf-8")
                self.wfile.write(resposta)


    def do_POST(self):
        # lê o corpo apenas uma vez
        try:
            tamanho = int(self.headers.get('Content-Length', 0))
            corpo = self.rfile.read(tamanho).decode('utf-8') if tamanho > 0 else ''
            dados = parse_qs(corpo)
        except Exception as e:
            resposta = json.dumps({"erro": f"Erro lendo corpo: {e}"}).encode('utf-8')
            self.send_response(400)
            self.send_header("Content-type", "application/json")
            self.send_header("Content-Length", str(len(resposta)))
            self.end_headers()
            self.wfile.write(resposta)
            return

        try:
            # usa path parse para consistência com do_GET, sem alterar do_GET
            caminho = urlparse(self.path).path

            if caminho == "/produto/criar":
                codigo = dados.get('codigo', [None])[0]
                nome = dados.get('nome', [None])[0]
                preco = dados.get('preco', [None])[0]
                quantidade = dados.get('quantidade', [None])[0]

                if None in (codigo, nome, preco, quantidade):
                    resposta = json.dumps({"erro": "Dados incompletos para criação"}).encode('utf-8')
                    self.send_response(400)
                    self.send_header("Content-type", "application/json")
                    self.send_header("Content-Length", str(len(resposta)))
                    self.end_headers()
                    self.wfile.write(resposta)
                    return

                try:
                    preco_v = float(preco)
                except ValueError:
                    preco_v = 0.0
                try:
                    quantidade_v = int(quantidade)
                except ValueError:
                    quantidade_v = 0

                produto = Produto(codigo, nome, preco_v, quantidade_v)
                try:
                    servico.adicionarProduto(produto)
                except Exception as e:
                    resposta = json.dumps({"erro": f"Erro ao adicionar produto: {e}"}).encode('utf-8')
                    self.send_response(500)
                    self.send_header("Content-type", "application/json")
                    self.send_header("Content-Length", str(len(resposta)))
                    self.end_headers()
                    self.wfile.write(resposta)
                    return

                resposta = json.dumps({"sucesso": "Produto adicionado"}).encode('utf-8')
                self.send_response(201)
                self.send_header("Content-type", "application/json")
                self.send_header("Content-Length", str(len(resposta)))
                self.end_headers()
                self.wfile.write(resposta)
                return

            elif caminho == "/produto/deletar":
                codigo = dados.get("codigo", [None])[0]

                if codigo is None:
                    resposta = json.dumps({"erro": "Dados incompletos para exclusão"}).encode('utf-8')
                    self.send_response(400)
                    self.send_header("Content-type", "application/json")
                    self.send_header("Content-Length", str(len(resposta)))
                    self.end_headers()
                    self.wfile.write(resposta)
                    return

                try:
                    servico.deletarProduto(codigo)
                except Exception as e:
                    # apenas loga erro interno, mas ainda retorna 200 para o cliente
                    print(f"Erro interno ao deletar: {e}")

                resposta = json.dumps({"sucesso": "Produto removido"}).encode('utf-8')
                self.send_response(200)
                self.send_header("Content-type", "application/json")
                self.send_header("Content-Length", str(len(resposta)))
                self.end_headers()
                self.wfile.write(resposta)
                return

            elif caminho == "/produto/atualizar":
                codigo = dados.get('codigo', [None])[0]
                nome = dados.get('nome', [None])[0]
                preco = dados.get('preco', [None])[0]
                quantidade = dados.get('quantidade', [None])[0]

                if None in (codigo, nome, preco, quantidade):
                    resposta = json.dumps({"erro": "Dados incompletos para criação"}).encode('utf-8')
                    self.send_response(400)
                    self.send_header("Content-type", "application/json")
                    self.send_header("Content-Length", str(len(resposta)))
                    self.end_headers()
                    self.wfile.write(resposta)
                    return
                
                produto = Produto(codigo, nome, preco, quantidade)

                try:
                    atualizado = servico.atualizarProduto(produto)
                except Exception as e:
                    resposta = json.dumps({"erro": f"Erro ao atualizar produto: {e}"}).encode('utf-8')
                    self.send_response(500)
                    self.send_header("Content-type", "application/json")
                    self.send_header("Content-Length", str(len(resposta)))
                    self.end_headers()
                    self.wfile.write(resposta)
                    return

                if not atualizado:
                    resposta = json.dumps({"erro": "Produto não encontrado"}).encode('utf-8')
                    self.send_response(404)
                    self.send_header("Content-type", "application/json")
                    self.send_header("Content-Length", str(len(resposta)))
                    self.end_headers()
                    self.wfile.write(resposta)
                    return

                resposta = json.dumps({"sucesso": "Produto atualizado"}).encode('utf-8')
                self.send_response(200)
                self.send_header("Content-type", "application/json")
                self.send_header("Content-Length", str(len(resposta)))
                self.end_headers()
                self.wfile.write(resposta)
                return

            
            else:
                resposta = json.dumps({"erro": "Caminho POST não encontrado"}).encode('utf-8')
                self.send_response(404)
                self.send_header("Content-type", "application/json")
                self.send_header("Content-Length", str(len(resposta)))
                self.end_headers()
                self.wfile.write(resposta)
                return

        except Exception as e:
            resposta = json.dumps({"erro": f"Erro interno: {e}"}).encode('utf-8')
            self.send_response(500)
            self.send_header("Content-type", "application/json")
            self.send_header("Content-Length", str(len(resposta)))
            self.end_headers()
            self.wfile.write(resposta)




def main():
    # força ligação em 127.0.0.1 (IPv4) para evitar problemas com resolução localhost IPv6/IPv4
    servidor = HTTPServer(('127.0.0.1', 8080), Provider)
    print("Servidor iniciado em http://127.0.0.1:8080")
    servidor.serve_forever()

if __name__ == "__main__":
    main()