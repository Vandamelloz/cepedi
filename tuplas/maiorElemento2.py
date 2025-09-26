'''dados = ("João", 25, "Engenheiro", ("Python", "C++", "Java"))
print(dados[3][0])
#desempacotar tuplas
dados = ("Maria", 32, "Professora", "São Paulo")
nome=dados[0]
idade=dados[1]
profissao=dados[2]
cidade=dados[3]
print(nome, idade, profissao, cidade)'''
#tupla dentro da lista 
lista2=[]
lista = [(1, 2), (3, 4), (5, 6)]
print(lista[1][1]) #acessando elemento diretamente 
#Como somar todos os segundos elementos de cada tupla usando um for?
for i in lista:
 lista2.append(sum(i))
print(lista2)

'''tupla=(1, 2, 80, 70, 60)
a = (1, 2, 3) + (4, 5)
b = (1, 2, 3) * 2
print(a)
print(b)'''

'''sorte=sorted(tupla, reverse=True)
print(sorte)
print(sorte[1])'''
