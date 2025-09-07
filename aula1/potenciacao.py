'''11. Crie um programa em Python que solicite ao usuário dois números inteiros e, em
seguida, imprima o resultado da potenciação do primeiro pelo segundo. Usar o módulo
math.
'''
import math
numero1=int(input("Digite o número 1: "))
numero2=int(input("Digite o número 2:"))
print(f"A potenciação do n°1 pelo n°2: {math.pow(numero1, numero2)}")
'''
| Função (em `math`) | O que faz                                 | Exemplo de uso            |
| ------------------ | ----------------------------------------- | ------------------------- |
| `math.fabs(x)`     | Retorna o valor absoluto (sempre `float`) | `math.fabs(-5) → 5.0`     |
| `math.sqrt(x)`     | Raiz quadrada                             | `math.sqrt(16) → 4.0`     |
| `math.pow(x, y)`   | Potência $x^y$ (sempre `float`)           | `math.pow(2, 3) → 8.0`    |
| `math.exp(x)`      | Exponencial $e^x$                         | `math.exp(1) → 2.718...`  |
| `math.log(x)`      | Logaritmo natural (base $e$)              | `math.log(10) → 2.302...` |
| `math.log10(x)`    |                                           |                           |

'''