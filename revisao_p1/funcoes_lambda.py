#Funções anônimas, não precisa definir a função 
preco=1000
calcular_imposto= lambda preco: preco*0.3
print(calcular_imposto(preco))
#antes dos : o que ela vai receber como valor, após; o que ela vai retornar
precos=[100, 200, 1500, 450]
impostos= tuple(map(lambda preco: preco*0.5, precos))
print(impostos)
#variavel= list(map(funcao, lista))
#o map irá pegar a lista e transformar cada um desses valores com uma função 
