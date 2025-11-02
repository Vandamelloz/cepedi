import sqlite3 
try:
 banco= sqlite3.connect('primeiro_banco.db')

 cursor= banco.cursor() 

 cursor.execute("DELETE FROM pessoas where idade=vanda")
 banco.commit()
 banco.close() #fecha a conexão com o banco 
 print("Os dados de Patricia foram removidos com sucesso!")

except sqlite3.Error as erro: 
 print("Erro ao excluir os dados de Patricia: ", erro)
