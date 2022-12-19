CREATE DATABASE ampare

USE ampare
CREATE TABLE Alimento (
 id INT,
 cesta_id INT,
 tipo_alimento_id INT,
 data_validade DATE
);

USE ampare
CREATE TABLE Familia (
 id INT,
 nome VARCHAR(50),
 tamanho INT,
 endereco VARCHAR(50)
);

USE ampare
CREATE TABLE Cesta (
 id INT,
 id_familia INT,
 status VARCHAR(10),
 entrega_id INT,
);

USE ampare
CREATE TABLE TipoAlimento (
 id INT,
 nome VARCHAR(50),
 peso FLOAT(10),
 descricao VARCHAR(50)
);

USE ampare
CREATE TABLE Entrega (
 id INT,
 id_familia INT,
 endereco VARCHAR(10),
 data DATE,
 hora TIME
);
