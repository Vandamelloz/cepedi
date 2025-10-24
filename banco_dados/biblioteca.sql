CREATE TABLE IF NOT EXISTS autores (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    nome TEXT,
    data_nascimento TEXT
);

CREATE TABLE IF NOT EXISTS editoras (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    nome TEXT,
    cidade TEXT
);

CREATE TABLE IF NOT EXISTS livros (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    titulo TEXT,
    ano_publicacao TEXT,
    editoras_id INTEGER NOT NULL,
    autores_id INTEGER NOT NULL,
    FOREIGN KEY (editoras_id) REFERENCES editoras(id),
    FOREIGN KEY (autores_id) REFERENCES autores(id)
);

CREATE TABLE IF NOT EXISTS usuario (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    nome TEXT,
    email TEXT,
    telefone TEXT
);

CREATE TABLE IF NOT EXISTS emprestimos (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    data_emprestimo DATE,
    data_devolucao DATE,
    usuario_id INTEGER NOT NULL,
    livros_id INTEGER NOT NULL,
    FOREIGN KEY (usuario_id) REFERENCES usuario(id),
    FOREIGN KEY (livros_id) REFERENCES livros(id)
);

INSERT INTO editoras (nome, cidade) VALUES
('Editora Alfa', 'São Paulo'),
('Editora Beta', 'Rio de Janeiro'),
('Editora Gama', 'Curitiba'),
('Editora Delta', 'Belo Horizonte'),
('Editora Epsilon', 'Porto Alegre'),
('Editora Zeta', 'Brasília'),
('Editora Eta', 'Recife'),
('Editora Theta', 'Salvador'),
('Editora Iota', 'Fortaleza'),
('Editora Kappa', 'Manaus'),
('Editora Lambda', 'Campinas'),
('Editora Mu', 'Florianópolis'),
('Editora Nu', 'Natal'),
('Editora Xi', 'João Pessoa'),
('Editora Omicron', 'Maceió'),
('Editora Pi', 'Cuiabá'),
('Editora Rho', 'Campo Grande'),
('Editora Sigma', 'São Luís'),
('Editora Tau', 'Aracaju'),
('Editora Upsilon', 'Goiânia');

INSERT INTO autores (nome, data_nascimento) VALUES
('João Silva', '1970-05-12'),
('Maria Souza', '1985-07-30'),
('Carlos Pereira', '1968-11-22'),
('Ana Lima', '1990-01-15'),
('Lucas Fernandes', '1975-03-18'),
('Beatriz Alves', '1982-09-09'),
('Ricardo Costa', '1960-12-02'),
('Fernanda Rocha', '1995-04-28'),
('Marcos Dias', '1988-06-10'),
('Juliana Martins', '1979-10-25'),
('Paulo Gomes', '1965-02-17'),
('Carla Nunes', '1992-08-03'),
('Eduardo Ribeiro', '1973-07-11'),
('Sandra Lima', '1980-05-29'),
('Felipe Santana', '1987-11-06'),
('Patrícia Melo', '1969-12-21'),
('Rafael Alves', '1991-03-04'),
('Luciana Torres', '1983-09-15'),
('Gustavo Silva', '1978-01-19'),
('Vanessa Moreira', '1994-10-12');

INSERT INTO livros (titulo, ano_publicacao, editoras_id, autores_id) VALUES
('O Mundo Novo', '2000', 1, 1),
('A Vida em Cores', '2005', 2, 2),
('Segredos do Tempo', '2010', 3, 3),
('Além do Horizonte', '2015', 4, 4),
('Noite Estrelada', '2020', 5, 5),
('Caminhos Cruzados', '1999', 6, 6),
('Ventos do Norte', '2003', 7, 7),
('Jardim Secreto', '2007', 8, 8),
('Sombras da Alma', '2011', 9, 9),
('Mar de Esperança', '2016', 10, 10),
('Cidade Perdida', '2018', 11, 11),
('Luz e Escuridão', '2021', 12, 12),
('Ecos do Passado', '2004', 13, 13),
('Coração Selvagem', '2008', 14, 14),
('A Última Canção', '2012', 15, 15),
('Som do Silêncio', '2017', 16, 16),
('Rosas e Espinhos', '2019', 17, 17),
('Almas Gêmeas', '2022', 18, 18),
('No Ritmo do Coração', '2006', 19, 19),
('Além das Estrelas', '2014', 20, 20);

INSERT INTO usuario (nome, email, telefone) VALUES
('Ana Paula', 'ana.paula@email.com', '11987654321'),
('Bruno Silva', 'bruno.silva@email.com', '21987654321'),
('Carla Mendes', 'carla.mendes@email.com', '31987654321'),
('Daniel Costa', 'daniel.costa@email.com', '41987654321'),
('Elisa Freitas', 'elisa.freitas@email.com', '51987654321'),
('Fabio Lima', 'fabio.lima@email.com', '61987654321'),
('Gabriela Souza', 'gabriela.souza@email.com', '71987654321'),
('Hugo Martins', 'hugo.martins@email.com', '81987654321'),
('Isabela Rocha', 'isabela.rocha@email.com', '91987654321'),
('João Pedro', 'joao.pedro@email.com', '11987654322'),
('Karina Alves', 'karina.alves@email.com', '21987654322'),
('Leonardo Dias', 'leonardo.dias@email.com', '31987654322'),
('Mariana Lima', 'mariana.lima@email.com', '41987654322'),
('Nicolas Costa', 'nicolas.costa@email.com', '51987654322'),
('Olivia Fernandes', 'olivia.fernandes@email.com', '61987654322'),
('Pedro Henrique', 'pedro.henrique@email.com', '71987654322'),
('Quésia Rocha', 'quesia.rocha@email.com', '81987654322'),
('Ricardo Moreira', 'ricardo.moreira@email.com', '91987654322'),
('Sabrina Nunes', 'sabrina.nunes@email.com', '11987654323'),
('Thiago Silva', 'thiago.silva@email.com', '21987654323');

INSERT INTO emprestimos (data_emprestimo, data_devolucao, usuario_id, livros_id) VALUES
('2024-01-05', '2024-01-15', 1, 5),
('2024-01-07', '2024-01-20', 2, 3),
('2024-01-08', '2024-01-18', 3, 1),
('2024-01-10', '2024-01-25', 4, 4),
('2024-01-12', '2024-01-22', 5, 6),
('2024-01-15', '2024-01-30', 6, 2),
('2024-01-17', '2024-01-27', 7, 8),
('2024-01-20', '2024-02-05', 8, 9),
('2024-01-22', '2024-02-01', 9, 7),
('2024-01-25', '2024-02-10', 10, 10),
('2024-01-27', '2024-02-07', 11, 11),
('2024-01-30', '2024-02-15', 12, 12),
('2024-02-01', '2024-02-20', 13, 13),
('2024-02-05', '2024-02-18', 14, 14),
('2024-02-07', '2024-02-22', 15, 15),
('2024-02-10', '2024-02-25', 16, 16),
('2024-02-12', '2024-02-28', 17, 17),
('2024-02-15', '2024-03-01', 18, 18),
('2024-02-18', '2024-03-05', 19, 19),
('2024-02-20', '2024-03-10', 20, 20);

select * from autores;
select * from livros;
select * from editoras;
select * from usuario;
select * from emprestimos;
select titulo from livros where autores_id=(
    select id from autores where nome="João Silva"
);

