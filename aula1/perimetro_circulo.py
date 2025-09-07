'''15. Crie um programa em Python que solicite ao usuário o raio e calcule e imprima o
perímetro e a área do círculo correspondente. Usar o módulo math.
'''
import math
raio=float(input("Digite o raio do círculo: "))
area=math.pi*raio**2
perimetro= (math.pi*2)*raio
print(f"A área do seu círculo é de: {area}, e o perímetro è: {perimetro}")