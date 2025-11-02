import sqlite3 
nome="Clara"
idade=23
email="clara908@hotmail.com"

teste= sqlite3.connect('primeiro_banco.db')

cursor= teste.cursor()

# cursor.execute("INSERT INTO pessoas VALUES('"+nome+"', "+str(idade)+", '"+email+"')")
# teste.commit()
# cursor.execute("UPDATE pessoas SET nome= 'Júlia' where idade=24")
# teste.commit()
# cursor.execute("ALTER TABLE pessoas ADD COLUMN profissao text")
# teste.commit()
# cursor.execute("UPDATE pessoas SET profissao = 'Professor de Dança' WHERE nome = 'Carlos'")
# cursor.execute("UPDATE pessoas SET profissao = 'Instrutora de Ballet' WHERE nome = 'Mariana'")
# cursor.execute("UPDATE pessoas SET profissao = 'Coreógrafo' WHERE nome = 'João Pedro'")
# cursor.execute("UPDATE pessoas SET profissao = 'Aluna de Dança Contemporânea' WHERE nome = 'Beatriz'")
# cursor.execute("UPDATE pessoas SET profissao = 'Instrutor de Ritmos Urbanos' WHERE nome = 'Lucas'")
# cursor.execute("UPDATE pessoas SET profissao = 'Professora de Jazz' WHERE nome = 'Vanda'")
# cursor.execute("UPDATE pessoas SET profissao = 'Músico e Dançarino' WHERE nome = 'Gabriel'")
# cursor.execute("UPDATE pessoas SET profissao = 'Aluna de Dança Clássica' WHERE nome = 'Larissa'")
# cursor.execute("UPDATE pessoas SET profissao = 'Coordenador Artístico' WHERE nome = 'Ricardo'")
# cursor.execute("UPDATE pessoas SET profissao = 'Assistente de Palco' WHERE nome = 'Juliana'")
# cursor.execute("UPDATE pessoas SET profissao = 'Bailarina Estagiária' WHERE nome = 'Rafaela'")
# cursor.execute("UPDATE pessoas SET profissao = 'Fotógrafo de Espetáculos' WHERE nome = 'Felipe'")p as SELECT DISTINCT(nome text, idade integer, email text) FRO
# cursor.execute("UPDATE pessoas SET profissao = 'Produtora Cultural' WHERE nome = 'Camila'")
# cursor.execute("UPDATE pessoas SET profissao = 'Instrutor de Danças Latinas' WHERE nome = 'Thiago'")
# cursor.execute("UPDATE pessoas SET profissao = 'Iluminador Cênico' WHERE nome = 'Eduardo'")
# cursor.execute("UPDATE pessoas SET profissao = 'Secretária da Escola' WHERE nome = 'Clara'")
# cursor.execute("UPDATE pessoas SET profissao = 'Músico Instrumentista' WHERE nome = 'Mateus'")
# cursor.execute("UPDATE pessoas SET profissao = 'Dançarina de Jazz' WHERE nome = 'Sabrina'")
# cursor.execute("UPDATE pessoas SET profissao = 'Administrador' WHERE nome = 'André'")
# cursor.execute("UPDATE pessoas SET profissao = 'Figurinista' WHERE nome = 'Carla'")
# teste.commit()

#APAGAR REINCIDÊNCIAS 
# cursor.execute(
# """
# CREATE TABLE pessoas_temp as SELECT DISTINCT nome text, idade integer, email text
# FROM pessoas
# """
# )
# teste.commit()
# cursor.execute(
#     """
# DROP TABLE pessoas
# """
# )
# cursor.execute(
#     """
# ALTER TABLE pessoas_temp RENAME TO pessoas
# """
# )
# teste.commit()
# cursor.execute(
#  """
# DELETE FROM pessoas where text='carlos'
# """
# )
# teste.commit()
cursor.execute("PRAGMA table_info(pessoas)")
# print(cursor.fetchall())
# cursor.execute(
# """
# ALTER TABLE pessoas RENAME COLUMN text TO nome
# """
# )
# teste.commit()
# cursor.execute(
# """
# ALTER TABLE pessoas RENAME COLUMN integer TO idade
# """
# )
# cursor.execute(
# """
# ALTER TABLE pessoas RENAME COLUMN TEXT TO email
# """
# )
# teste.commit()
#PRAGMA table_info= desc do mysql
cursor.execute("PRAGMA table_info (pessoas)")
print(cursor.fetchall())