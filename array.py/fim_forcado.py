lista_livros=[]
i=1
lista_livros.append(input("Digite o nome de um livro: "))
lista_livros.insert(1, input("Digite o nome do livro 2: "))
'''while i<=2:
  lista_livros.append(input("Digite o nome de um livro: "))
  lista_livros.insert(1, input("Digite o nome do livro 2: "))
  i+=1'''
print(lista_livros)
remove= input("Qual livro deseja remover? ")
lista_livros.remove(remove)
print(lista_livros)

  




