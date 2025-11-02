with open('revisao_p1/textosplit.txt','r', encoding='UTF-8') as arquivo: 
 #abrir o arquivo para leitura: w pode ser utilizada para sobreescrever no arquivo
 texto=arquivo.read()
#  print(texto)

 palavras= texto.split() #separar o texto sempre que ver um espaço
#  print(palavras)
#  for palavra in palavras:
#   if '.' in palavra or ':' in palavra or ',' in palavra:
#     print(palavra[:-1])
#  else:
#   print(palavra)
#   if '..' in palavra:
#    print(palavra[:-2])
print(palavras.count('cinza')) #quantas vezes uma palavra se repete no texto
# palavras_virg= texto.split(',')
# for palavra in palavras_virg:
#  print(palavra)
#SEPARAR TEXTO EM LINHAS
linhas=texto.split('/n')

for palavra in linhas:
 print(palavra)
 
