codigo=int(input("Insira um código de 1 a 30: "))
if codigo>=1 and codigo<=10:
    print("Código do setor alimentação!")
elif codigo>=11 and codigo<=20:
    print("Código do setor limpeza!")
elif codigo>=21 and codigo <=30:
     print("Código do setor eletrônicos!") 
else:
     print("Código não encontrado!")
