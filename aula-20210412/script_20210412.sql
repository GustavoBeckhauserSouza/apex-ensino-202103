# Chave primária chave estrangeira
# Normalização de tabelas
# Tipos de relacionamento (1:1, 1:N, N:N)

CREATE DATABASE IF NOT EXISTS aula_20210412;
USE aula_20210412;

# Uma chave primária é uma (ou mais de uma) coluna em uma tabela que
# servirá como identificador único daquele registro.
# Também serve como link entre 2 tabelas
# Por definição, uma chave primária nunca repete o seu valor

CREATE TABLE IF NOT EXISTS clientes(
	id INT NOT NULL, sobrenome VARCHAR(100) NOT NULL,
    nome VARCHAR(30) NOT NULL, idade TINYINT UNSIGNED,
    PRIMARY KEY(id)
);

INSERT INTO clientes(id, sobrenome, nome, idade) VALUES (
	1, "dos Santos", "Maria", 32
);
INSERT INTO clientes(id, sobrenome, nome, idade) VALUES (
	2, "dos Santos", "Maria", 32
);
UPDATE clientes SET nome = "José", sobrenome = "da Silva" WHERE id = 2;
SELECT * FROM clientes;

# Podemos também alterar uma tabela, inserindo ou removendo uma
# chave primária existente.
CREATE TABLE IF NOT EXISTS produtos(
	id INT NOT NULL, nome VARCHAR(50) NOT NULL, preco FLOAT
);


ALTER TABLE produtos ADD PRIMARY KEY(id);
DESC produtos;
ALTER TABLE produtos DROP PRIMARY KEY;

# É possível criar um campo do tipo chave primária que auto
# incremente o seu valor todas as vezes que um registro for adicionado.
CREATE TABLE IF NOT EXISTS pedidos(
	id INT NOT NULL AUTO_INCREMENT, valor FLOAT NOT NULL, PRIMARY KEY(id)
);
DESC pedidos;

# Quando uma coluna é do tipo auto_increment, não precisamos informar
# o seu id, ele será gerado de forma automática
INSERT INTO pedidos(valor) VALUES (1200);
INSERT INTO pedidos(valor) VALUES (850);
INSERT INTO pedidos(valor) VALUES (789.68);

DESC pedidos;
SELECT * FROM pedidos;

# Utilizamos as chaves estrangeiras quando queremos referenciar na
# nossa tabela, um valor(coluna) que está em outra tabela
CREATE TABLE IF NOT EXISTS carrinho_de_compras(
	id INT NOT NULL PRIMARY KEY AUTO_INCREMENT,
    cliente_id INT NOT NULL,
    info VARCHAR(100),
    FOREIGN KEY(cliente_id) REFERENCES clientes(id)
);

INSERT INTO carrinho_de_compras(cliente_id, info) VALUES (
	1, "Carrinho criado em Dezembro"
);

INSERT INTO carrinho_de_compras(cliente_id, info) VALUES (
	1, "Carrinho atual"
);

INSERT INTO carrinho_de_compras(cliente_id, info) VALUES (
	2, "Primeiro carrinho"
);

SELECT * FROM carrinho_de_compras;

# Mostrando dados de 2 tabelas relacionadas
SELECT
	clientes.id, clientes.nome,
    clientes.sobrenome, carrinho_de_compras.id,
    carrinho_de_compras.info
FROM clientes
INNER JOIN carrinho_de_compras
	ON clientes.id = carrinho_de_compras.cliente_id;
    

INSERT INTO carrinho_de_compras(cliente_id, info) VALUES (
	5, "Carrinho desconhecido."
);