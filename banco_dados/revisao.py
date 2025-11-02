import sqlite3 

banco= sqlite3.connect('primeiro_banco.db')

cursor= banco.cursor() #objeto cursor recebe o objeto do banco e atráves do cursos utilizar os comandos sql

# cursor.execute("CREATE TABLE pessoas(nome text, idade integer, email text)")
# cursor.execute("INSERT INTO pessoas values('Vanda', 21, 'vandabarsa2004@gmail.com')")
# banco.commit()
# cursor.execute("INSERT INTO pessoas values('carlos', 32, 'carlosbd@gmail.com')")
# banco.commit()
# cursor.exec ute("DELETE FROM pessoas where idade=32")
# banco.commit()
# cursor.execute("""
# INSERT INTO pessoas (nome, idade, email) VALUES
# ('Carlos', 32, 'carlosbd@gmail.com'),
# ('Mariana', 25, 'mariana.silva@gmail.com'),
# ('João Pedro', 28, 'joaopedro28@hotmail.com'),
# ('Beatriz', 22, 'bia_melo@gmail.com'),
# ('Lucas', 35, 'lucas.ribeiro@gmail.com'),
# ('Fernanda', 27, 'fernandaa.lima@hotmail.com'),
# ('Gabriel', 30, 'gabriel.torres@gmail.com'),
# ('Larissa', 26, 'lari_oliveira@gmail.com'),
# ('Ricardo', 40, 'ricardo.santos@gmail.com'),
# ('Amanda', 24, 'amanda.souza@gmail.com'),
# ('Rafaela', 21, 'rafa.menezes@hotmail.com'),
# ('Felipe', 29, 'felipe.alves@gmail.com'),
# ('Camila', 33, 'camila.freitas@gmail.com'),
# ('Thiago', 31, 'thiago.moura@gmail.com'),
# ('Juliana', 23, 'juliana.pires@gmail.com'),
# ('Eduardo', 36, 'eduardo.azevedo@gmail.com'),
# ('Patrícia', 27, 'patricia.lopes@gmail.com'),
# ('Mateus', 34, 'mateus.barbosa@gmail.com'),
# ('Sabrina', 25, 'sabrina.coelho@hotmail.com'),
# ('André', 38, 'andre.martins@gmail.com');
# """)
# banco.commit()
banco.close
cursor.execute("SELECT * FROM pessoas")
print(cursor.fetchall())