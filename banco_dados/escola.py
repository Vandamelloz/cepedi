import sqlite3

def escola():
    con = sqlite3.connect("banco_escola.db")
    cur = con.cursor()

    # Criar tabela de cursos
    cur.execute("""
    CREATE TABLE IF NOT EXISTS Curso (
        codigo INTEGER NOT NULL,
        nome TEXT NOT NULL,
        area TEXT
        PRIMARY KEY()
    );
    """)

    # Criar tabela de professores
    cur.execute("""
    CREATE TABLE IF NOT EXISTS Professor (
        cpf TEXT PRIMARY KEY,
        nome TEXT NOT NULL,
        data_nascimento DATE
    );
    """)

    # Criar tabela de alunos
    cur.execute("""
    CREATE TABLE IF NOT EXISTS Aluno (
        matricula TEXT PRIMARY KEY,
        curso_codigo INTEGER NOT NULL,
        nome TEXT NOT NULL,
        endereco TEXT,
        FOREIGN KEY (curso_codigo) REFERENCES Curso(codigo)
    );
    """)

    # Criar tabela Curso_Professor
    cur.execute("""
    CREATE TABLE IF NOT EXISTS Curso_Professor (
        curso_codigo INTEGER NOT NULL,
        professor_cpf TEXT NOT NULL,
        PRIMARY KEY (curso_codigo, professor_cpf),
        FOREIGN KEY (curso_codigo) REFERENCES Curso(codigo),
        FOREIGN KEY (professor_cpf) REFERENCES Professor(cpf)
    );
    """)

    # Inserir cursos
    cursos = [
        (101, "Engenharia de Software", "Tecnologia"),
        (102, "Medicina", "Saúde"),
        (103, "Direito", "Humanas"),
        (104, "Arquitetura", "Exatas")
    ]
    cur.executemany("INSERT OR IGNORE INTO Curso (codigo, nome, area) VALUES (?, ?, ?)", cursos)

    # Inserir professores
    professores = [
        ("12345678901", "Carlos Silva", "1975-05-10"),
        ("98765432100", "Ana Maria", "1980-08-22"),
        ("11122233344", "João Pedro", "1969-03-15"),
        ("55566677788", "Luciana Rocha", "1990-12-01")
    ]
    cur.executemany("INSERT OR IGNORE INTO Professor (cpf, nome, data_nascimento) VALUES (?, ?, ?)", professores)

    # Inserir alunos
    alunos = [
        ("20230001", 101, "Marcos Almeida", "Rua A, 123"),
        ("20230002", 102, "Fernanda Costa", "Av. Brasil, 456"),
        ("20230003", 101, "Lucas Pereira", "Rua das Flores, 789"),
        ("20230004", 103, "Juliana Souza", "Travessa Central, 101")
    ]
    cur.executemany("INSERT OR IGNORE INTO Aluno (matricula, curso_codigo, nome, endereco) VALUES (?, ?, ?, ?)", alunos)

    # Inserir curso_professor
    curso_professor = [
        (101, "12345678901"),
        (101, "98765432100"),
        (102, "11122233344"),
        (103, "55566677788")
    ]
    cur.executemany("INSERT OR IGNORE INTO Curso_Professor (curso_codigo, professor_cpf) VALUES (?, ?)", curso_professor)

    # Leitura dos alunos cadastrados
    print("\nAlunos cadastrados:")
    cur.execute("SELECT matricula, nome, endereco FROM Aluno")
    alunos = cur.fetchall()
    for aluno in alunos:
        print(aluno)

    # Finaliza conexão
    con.commit()
    con.close()

# Chamada da função principal
if __name__ == "__main__":
    escola()
