import math
a=float(input("Digite um número: "))
print(f"A parte fracionária do seu número é: {a-int(a)}")
frac, inteiro= math.modf(a)
print(a)
'''14. Crie um programa em Python que peça ao usuário para inserir um número decimal e,
em seguida, calcule e imprima a parte fracionária desse número.
'''