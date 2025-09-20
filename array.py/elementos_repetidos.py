lista=["Maça", "Maça", "Uva", "Melão", "Maça"]
print(lista)
'''lista.remove("Maça")
print(lista)
print(lista[1])'''
for listas in lista:
  tamanho=len(lista)
  lista.remove("Maça")
  tamanhoafter=len(lista)
  if tamanho==tamanhoafter:
    break
print(lista)
#fazer um c´dogio que devolve os alimentos dalista sem repetições


