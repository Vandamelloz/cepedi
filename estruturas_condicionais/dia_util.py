print("1-Segunda-feira.")
print("2-Terça-feira.")
print("3-Quarta-feira.")
print("4-Quinta-feira.")
print("5-Sexta-feira.")
print("6-Sábado.")
print("7-Domingo.")
dia=int(input("Digite um número de 1 a 7 que represente um dia da semana: "))
if dia>=1 and dia<=5:
    print("Dia útil da semana!")
elif dia==7 or dia==6:
    print("Final de semana!")
else:
    print("Dia não reconhecido!")
