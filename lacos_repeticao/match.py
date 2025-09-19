dia=int(input("Digite um dia de 0 a 7: "))

'''def greet(person):
    match person:
        case "Alice":
            print("Olá, Alice!")
        case "Bob":
            print("Olá, Bob!")
        case _: # Caso padrão
            print("Olá, estranho!")

greet("Alice") # Saída: Olá, Alice!
greet("Charlie") # Saída: Olá, estranho!'''
def greet(dia):
    match dia:
       case 1:
          print("Segunda-feira!")
       case 2:
          print("Terça-feira!")
       case 3:
          print("Quarta-feira!")
       case 4:
          print("Quinta-feira!")
       case 5:
          print("Sexta-feira!")
       case 6:
          print("Sàbado!")
       case 7:
         print("Domingo!")


     
