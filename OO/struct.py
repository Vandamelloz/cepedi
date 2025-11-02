class Exame_conduzido:
 def __init__(self, id_aluno: int, conducaoResposta:int, abraco:int, mecanica:int, ritmo:int, 
              marcacao:int, id_professor:int):
   self.id_aluno=id_aluno
   self.conducaoResposta=conducaoResposta
   self.abraco=abraco
   self.mecanica=mecanica
   self.ritmo=ritmo
   self.marcacao=marcacao
   self.id_professor=id_professor
 def  __str__(self):
   return f"Exame_conduzido(id_aluno={self.id_aluno}, conducaoResposta={self.conducaoResposta}, abraco={self.abraco}, mecanica={self.mecanica}, ritmo={self.ritmo},
     marcacao={self.marcacao}, id_professor={self.id_professor})"

   """
Classe modelo para a tabela pessoa
# """
# from model.categoria import Categoria

# class Pessoa:
#     def __init__(self, id: int, nome: str, categoria: Categoria, email: str,
#                  idade: int | None = None, altura: float | None = None,
#                  peso: float | None = None, data_nascimento: str | None = None,
#                  ativo: bool = True, observacoes: str | None = None,
#                  telefone: str | None = None, momento_cadastro: str | None = None):
#         self.id = id
#         self.nome = nome
#         self.email = email
#         self.idade = idade
#         self.altura = altura
#         self.peso = peso
#         self.data_nascimento = data_nascimento
#         self.ativo = ativo
#         self.observacoes = observacoes
#         self.telefone = telefone
#         self.momento_cadastro = momento_cadastro
#         self.categoria = categoria
    
#     def __str__(self):
#         return (f"Pessoa(id={self.id}, nome='{self.nome}', "
#                 f"email='{self.email}', idade={self.idade}, "
#                 f"categoria_id={self.categoria.id})")
  
  
#         id_professor INTEGER NOT NULL,  
#         ConducaoResposta INTEGER NOT NULL,  
#         Abraco INTEGER NOT NULL,  
#         Mecanica INTEGER NOT NULL,  
#         Ritmo INTEGER NOT NULL,  
#         Marcacao INTEGER NOT NULL,
#         FOREIGN KEY (id_aluno) REFERENCES Aluno(id),
#         FOREIGN KEY (id_professor) REFERENCES Professor(id)

 

 

#   tabela_aluno = '''
#     CREATE TABLE IF NOT EXISTS Aluno (
#         id INTEGER NOT NULL,
#         Matricula INTEGER UNIQUE NOT NULL,
#         Nome VARCHAR(50) NOT NULL,  
#         Idade INTEGER,  
#         Nivel_Condutor VARCHAR(20),
#         Nivel_Conduzido VARCHAR(20),
#         Data_nivel DATE,  
#         PRIMARY KEY(id)
#     );
#     '''

#     # Nome, id, Avaliador
#     tabela_professor = '''
#     CREATE TABLE IF NOT EXISTS Professor (
#         Nome VARCHAR(50) NOT NULL,  
#         id INTEGER NOT NULL,  
#         Avaliador VARCHAR(20) NOT NULL,
#         PRIMARY KEY(id)
#     );
#     '''
#     #id_aluno, id_professor, Conducao/Resposta, Abraco, Mecanica, Ritmo, Marcacao
#     tabela_exame_condutor = '''
#     CREATE TABLE IF NOT EXISTS Exame_condutor (
#         id_aluno INTEGER NOT NULL,  
#         id_professor INTEGER NOT NULL,  
#         ConducaoResposta INTEGER NOT NULL,  
#         Abraco INTEGER NOT NULL,  
#         Mecanica INTEGER NOT NULL,  
#         Ritmo INTEGER NOT NULL,  
#         Marcacao INTEGER NOT NULL,
#         FOREIGN KEY (id_aluno) REFERENCES Aluno(id),
#         FOREIGN KEY (id_professor) REFERENCES Professor(id)
#     );
#     '''
#     #id_aluno, id_professor, Conducao/Resposta, Abraco, Mecanica, Ritmo, Marcacao
#     tabela_exame_conduzido = '''
#     CREATE TABLE IF NOT EXISTS Exame_conduzido (
#         id_aluno INTEGER NOT NULL,  
#         id_professor INTEGER NOT NULL,  
#         ConducaoResposta INTEGER NOT NULL,  
#         Abraco INTEGER NOT NULL,  
#         Mecanica INTEGER NOT NULL,  
#         Ritmo INTEGER NOT NULL,  
#         Marcacao INTEGER NOT NULL,
#         FOREIGN KEY (id_aluno) REFERENCES Aluno(id),
#         FOREIGN KEY (id_professor) REFERENCES Professor(id)
#     );
#     '''
