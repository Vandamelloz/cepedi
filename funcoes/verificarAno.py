
ano=int(input("Digite um ano para ser verificado: "))
'''Um ano é bissexto se for divisível por 4, exceto nos anos terminados em 00, que precisam ser divisíveis por 400 para serem bissextos. Por exemplo, 2024 é bissexto por ser divisível por 4, enquanto 2100 não é bissexto por não ser divisível por 400, mesmo sendo divisível por 4. Divisibilidade por 400: Este ano só é bissexto se o número formado pelos dígitos anteriores aos zeros for divisível por 4. 
Exemplo: O ano 2000 foi bissexto porque 20 é divisível por 4. Já o ano 1900 não foi bissexto, pois 19 não é divisível por  Divisibilidade por 400: Este ano só é bissexto se o número formado pelos dígitos anteriores aos zeros for divisível por 4. 
Exemplo: O ano 2000 foi bissexto porque 20 é divisível por 4. Já o ano 1900 não foi bissexto, pois 19 não é divisível por 4'''
def anoBissexto(ano):
    bissexto=False
    if ano%4==0:
        bissexto=True
        numeroString= str(ano)
        if numeroString.endswith("00"): #função endswitch reconhece a terminação da string
          if ano%400==0:
            bissexto=True
          else:
             bissexto=False
    
    return bissexto
print(anoBissexto(ano))
        
    
