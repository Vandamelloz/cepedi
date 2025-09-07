a=int(input("Digite um valor a: "))
b=int(input("Digite o valor b: "))
print(a)
print(b)
a, b = b, a 
# polimorfismo diretamente
'''
temp=a
a=b
b=temp
'''
# backup temporário com o  auxilio de temp
print(f"Valor de a agora: {a}")
print(f"Valor de b agora: {b}")
# 5. Crie um programa em Python que solicite ao usuário 2 valores, em seguida, troque o
# valor dessas variáveis e imprima os novos valores.


