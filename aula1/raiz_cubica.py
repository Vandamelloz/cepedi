'''13. Crie um programa em Python que declare uma variável do tipo ponto flutuante e atribua
a ela um valor. Em seguida, calcule e imprima a raiz cúbica desse valor'''
import math
i=1
# do while forçado
while True:
 n1=int(input("Digite um número inteiro: "))
 print (f"A raiz cúbica de {n1} è de: {math.pow(n1, 1/3)}")
 i+=1

 if i>=5:
  break
