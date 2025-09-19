numero=1
for numero in range(1, 51):
    if numero %2!=0 and numero%3!=0 and numero%5!=0:
        print(f"{numero} é um número primo")
    else:
        print("O número não é primo!")