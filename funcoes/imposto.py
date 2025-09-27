valor=float(input("Digite o valor á ser acrescido o imposto: "))
imposto=0
def calcularImposto(valor):
   if valor>0 and valor<1000:
     imposto=valor*0.10
   elif valor<2000:
      imposto=valor*0.13
   else:
      imposto= valor*0.15
   return imposto
print(calcularImposto(valor))