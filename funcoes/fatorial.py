
def fatorial():
  fatorialB=1
  numero=int(input("Digite um número: "))
  for i in range(numero, 1, -1):
   fatorialB*=i
  print(f"O fatorial do seu número é: {fatorialB}")
fatorial()
 