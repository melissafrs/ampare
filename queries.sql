CREATE DATABASE ampare

USE ampare
CREATE TABLE Alimento (
 id INT IDENTITY(1,1) PRIMARY KEY,
 cesta_id INT,
 tipo_alimento_id INT,
 data_validade DATE
);

USE ampare
CREATE TABLE Familia (
 id INT IDENTITY(1,1) PRIMARY KEY,
 nome VARCHAR(50),
 tamanho INT,
 endereco VARCHAR(50)
);

USE ampare
CREATE TABLE Cesta (
 id INT IDENTITY(1,1) PRIMARY KEY,
 id_familia INT,
 status VARCHAR(10),
 entrega_id INT,
);

USE ampare
CREATE TABLE TipoAlimento (
 id INT IDENTITY(1,1) PRIMARY KEY,
 nome VARCHAR(50),
 peso FLOAT(10),
 descricao VARCHAR(50)
);

USE ampare
CREATE TABLE Entrega (
 id INT IDENTITY(1,1) PRIMARY KEY,
 id_familia INT,
 endereco VARCHAR(10),
 data DATE,
 hora TIME
);
