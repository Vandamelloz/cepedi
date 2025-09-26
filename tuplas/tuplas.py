dupla=((1, 2), (3,4), (9, 10))
'''lista=sum(dupla[0]), sum(dupla[1]), sum(dupla[2])'''
lista=[]
print(lista)
for i in dupla:
 lista.append(sum(i))

print(lista)
