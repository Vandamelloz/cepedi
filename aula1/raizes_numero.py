import math
a=float(input("Insira o valor de a: "))
b=float(input("Insira o valor de b: "))
c=float(input("Insira o valor de c: "))

delta=b**2-4*a*c
print(delta)
if delta<0:
 exit()
 
x1=(-b+math.sqrt(delta))/(2*a)
x2=(-b-math.sqrt(delta))/(2*a)
print(f"As raizes da sua equação são: {x1} e : {x2}")
