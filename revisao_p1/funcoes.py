 #função para fazer tratamento de erros 
produtos=[" ABC123", "  abcd11 ", "abc564"]
texto="abc11"

def tratar_texto(texto):
  texto=texto.upper()
  texto=texto.strip() #retira espaços antes e depois do texto
  return texto

texto2= "vandagsg"

texto2=tratar_texto(texto2)
print(texto2)

for i, produto in enumerate(produtos):
  produtos[i]=tratar_texto(produto) #ira receber o valor do indicie como parâmetro
print(produtos)
  

