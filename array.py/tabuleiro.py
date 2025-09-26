linhas= colunas=8
tabuleiro=''
for i in range(linhas):
    if i%2 ==0:
     for j in range(colunas): 
      if j %2 ==0:
        tabuleiro+="#"
      else:
       tabuleiro+=" "
print(tabuleiro)