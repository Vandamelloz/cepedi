# 12. Crie um programa em Python que declare uma variável do tipo ponto flutuante e atribua
# a ela um valor. Em seguida, calcule e imprima a raiz quadrada desse valor. Usar o módulo
# math.
import math
for i in range(1, 6):
 numero1=float(input(f"Insira o número: {i}: "))
 print(f"A raiz quadrada desse número é: {math.sqrt(numero1)}")
