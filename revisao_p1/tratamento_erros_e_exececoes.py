# try: #tentar executar
#   a=0
#   b=9
#   c=a/b
# except: #falhou execução
#  print("Tivemos um problema!")
# else: #execução funcionou
#   print(c)
# finally: #independente se deu certo ou não
#   print("Volte sempre!")
# try: #tentar executar
#   a=0
#   b=0
#   c=a/b
# except Exception as erro: #variável que mostra formatação
#  print(f"Tivemos um problema!{erro.__class__}")
# else: #execução funcionou
#   print(c)
# finally: #independente se deu certo ou não
#   print("Volte sempre!")

try: #tentar executar
  a=0
  b=0
  c=a/b
except (ValueError, TypeError): #falhou execução
 print("Tivemos um problema no tipo de dados!")
except ZeroDivisionError:
  print("Erro!Divisão por zero!!!")
except KeyboardInterrupt:
  print("O usuário prefere não indicar os dados!")
else: #execução funcionou
  print(c)
finally: #independente se deu certo ou não
  print("Volte sempre!")


   