raio=float(input("Insira o raio da base do seu clindro: "))
altura=float(input("Insira a altura: "))
base=3.14*(raio*raio)
area= 2*3.14*(raio + altura)
volume= (base*altura)*1000
print(f"A área do seu clindro é: {area}")
print(f"A base è: {base}")
print(f"Volume em litros: {volume}")