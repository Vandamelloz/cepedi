class Exame_conduzido:
 def __init__(self):
  self.id_aluno=""
  self.conducaoResposta=""
  self.abraco=""
  self.mecanica=""
  self.ritmo=""
  self.marcacao=""
  self.id_professor=""

  def __init__(self, id_aluno, conducaoResposta, abraco, mecanica, ritmo, marcacao, id_professor):
   self.id_aluno=id_aluno
   self.conducaoResposta=conducaoResposta
   self.abraco=abraco
   self.mecanica=mecanica
   self.ritmo=ritmo
   self.marcacao=marcacao
   self.id_professor=id_professor
  
  
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
