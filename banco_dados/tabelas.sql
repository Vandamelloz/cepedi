

create table if not exists proprietario(
    id integer not null,
    nome varchar(30),
    cidade varchar(30),
    primary key(id)
);
create table if not exists carro(
    id integer not null,
    modelo varchar(30) not null,
    ano varchar(30),
    proprietario_id integer not null,
    primary key(id)
    foreign key(proprietario_id) references proprietario(id)
);
insert into proprietario (nome, cidade) values ("Vanda", "Vitoria da Conquista");


select * from proprietario where nome like "%V%";

insert into proprietario(cidade, id, nome) values ("Brumado", 5, "Carla");


insert into proprietario(cidade, id, nome) values ("Itambé", 3, "Maria");

insert into proprietario(cidade, id, nome) values ("Itambé", 2, "João");
insert into proprietario(cidade, id, nome) values ("Itambé", 6, "Vitor");

INSERT INTO carro (id, modelo, ano, proprietario_id) VALUES (1, "Kombi", 1990, 1);
INSERT INTO carro (id, modelo, ano, proprietario_id) VALUES (2, "Chevette", 2000, 3);
INSERT INTO carro (id, modelo, ano, proprietario_id) VALUES (3, "Corolla", 2025, 7);
INSERT INTO carro (id, modelo, ano, proprietario_id) VALUES (4, "Civic", 2023, 7);
INSERT INTO carro (id, modelo, ano, proprietario_id) VALUES (7, "Nivus", 2022, 12);

select * from proprietario where id<4;
update proprietario set nome="Carla" where id=2;
select * from proprietario;
select * from proprietario, carro where proprietario.id= carro.proprietario_id ORDER BY ano ASC;






