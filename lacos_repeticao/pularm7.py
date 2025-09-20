numero=1
for numero in range(1, 101):
    if numero%7==0:
        continue
    print(f"Números não divisiveis por 7:{numero}")