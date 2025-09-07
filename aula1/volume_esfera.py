'''17. Crie um programa em Python que solicite ao usuário o valor do raio de uma esfera e
calcule e imprima o volume dessa esfera. Usar o módulo math.'''
import math
i=1
while i<=5:
 raio=float(input("Digite o raio da sua esfera: "))
 area_esfera=4*math.pi*raio**2
 volume_esfera=4/3*math.pi*raio**3
 print(f"A área da sua esfera é de: {area_esfera} e o volume é: {volume_esfera}")
 i+=1

