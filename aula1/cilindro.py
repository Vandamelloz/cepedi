import math
valor_pi = math.pi
raio=float(input("Insira o raio da base do seu clindro: "))
altura=float(input("Insira a altura: "))
base=valor_pi*(raio**2)
# area= 2*valor_pi*(raio + altura)
# print(f"A área do seu clindro é: {area}")
volume= (base*altura)*1000
print(f"A base è: {base}")
print(f"Volume em litros: {volume}")
'''16. Crie um programa em Python que solicite ao usuário o raio da base e a altura de uma
caixa d'água cilíndrica, calcule, e imprima na tela o seu volume em litros. Usar o módulo
math.
'''