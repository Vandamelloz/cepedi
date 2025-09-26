#criar uma tupla com 5 frutas
idades=(11, 10, 90, 20, 30)
frutas=("banana", "manga", "uva", "maça", "goiaba", "manga")
print(frutas)
#contar quantas vezes a repetida aparece na tupla
print(frutas.count("manga"))
print(frutas.count("Acerola")) #função da tupla
print(frutas.index("manga"))
print(max(idades))
print(min(idades))
print(max(frutas)) #retorna o último em ordem alfabética
print(min(frutas)) #retorna o primeiro em ordem alfabética 
tupla=(1, 2, 3, 4, 5, 6, 7, 8, 9, 9, 9)
lista=list(tupla)
print(lista)
tupla2= tuple(lista)
print(tupla2)
conjunto=set(tupla) #remove os elementos repetidos
print(conjunto)

'''mapa=map(tupla)
print(mapa)'''
soma=sum(idades)
print(soma/len(idades))
sorte=sorted(idades, reverse=True)
print(sorte)
#imprimir em ordfem decrescente







