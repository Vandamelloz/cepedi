'''10. Crie um programa em Python que solicite ao usuário um número decimal e, em seguida,
calcule e imprima o valor absoluto desse número. Usar o módulo math.'''
import math
numero=float(input("Digite um número decimal: "))
print(f"O valor absoluto deste número é: {math.fabs(numero)}")