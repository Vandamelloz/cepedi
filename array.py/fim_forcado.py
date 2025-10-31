# lista_livros=[]
# i=1
# lista_livros.append(input("Digite o nome de um livro: "))
# lista_livros.insert(1, input("Digite o nome do livro 2: "))
# '''while i<=2:
#   lista_livros.append(input("Digite o nome de um livro: "))
#   lista_livros.insert(1, input("Digite o nome do livro 2: "))
#   i+=1'''
# print(lista_livros)
# remove= input("Qual livro deseja remover? ")
# lista_livros.remove(remove)
# print(lista_livros)

# cadastro={}
# for i in range(0,2):
#   email=input("Digite o seu email: ")
#   senha=input("Digite sua senha: ")
#   cadastro[email]=senha

# print(cadastro)
cadastro={'email': 'senha'}
email=input("Digite o seu email: ")
senha=input("Digite sua senha: ")
try:
 if senha==cadastro[email]:
    print("Senha correta!")
 else:
    print("Senha incorreta!")
except KeyError:
  print("Chave não cadastrada")

  




