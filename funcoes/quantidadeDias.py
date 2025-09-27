ano=int(input("Digite o ano: "))
mes=int(input("Digite o mês: "))
mes31=(1, 3, 5, 7, 8, 10, 12)
mes30=(4, 6, 9, 11)
quantidade=0
def quantidadeDiasMes(ano, mes):
    bissexto=False
    if ano%4==0:
        bissexto=True
        numeroString= str(ano)
        if numeroString.endswith("00"): #função endswitch reconhece a terminação da string
          if ano%400==0:
            bissexto=True
          else:
             bissexto=False
    if bissexto==True:
       if mes==2:
          quantidade=29
    else:
       if mes==2:
          quantidade=28
    if mes in mes31:
       quantidade=31
    if mes in mes30:
       quantidade=30
    return quantidade
print(quantidadeDiasMes(ano, mes))
    