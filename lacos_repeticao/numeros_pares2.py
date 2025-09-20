n1=int(input("Digite o número 1:"))
n2=int(input("Digite o número 2: "))
if n1%2==1: n1+=1
for i in range(n1, n2, 2):
    print(i)
