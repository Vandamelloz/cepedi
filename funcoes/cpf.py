cpf=int(input("Digite o cpf: "))
def validarCpf(cpf):
 valido=False
 soma=0
 soma2=0
 dv=0
 dv2=0
 for i in range(9):
  soma+=int(cpf[i]) * (10-1)
 resto1=soma%11
 if resto1==0 or resto1==1:
  dv=1
  valido=False
 else:
  dv=11-resto1
  
 for i in range(10):
  soma2+=int(cpf[i]) * (11-1)
 resto2=soma2%11
 if resto2==1 or resto2==0:
  valido=True
  dv2=0
 else:
  dv2=11-resto2
 return valido
print(validarCpf(cpf))

