from classSgt import DataBaseCliente

database_1= DataBaseCliente(1234)
database_2=DataBaseCliente(6354)

print(database_1.get_connection())
print(database_2.get_connection())