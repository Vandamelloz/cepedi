class Pessoa:
    def __init(self, nome: str, idade: int):
        self.nome= nome
        self.idade=idade
    def __str__(self):
        return f"Pessoa(nome='{self.nome}', idade='{self.idade}')"
        



        """
Classe modelo para a tabela categoria
"""

# class Categoria: 
#     def __init__(self, id: int, nome: str):
#         self.id = id
#         self.nome = nome
    
#     def __str__(self):
#         return f"Categoria(id={self.id}, nome='{self.nome}')"