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
    
# Caso seja inserido um id que não existe na tabela pai, isso causará
# um erro de constraint, pois o id da tabela filha deve existir na
# tabela pai
INSERT INTO carrinho_de_compras(cliente_id, info) VALUES (
	5, "Carrinho desconhecido."
);

# --------------------------------------------------------------
# NORMALIZAÇÃO
# Anomalias são problemas que ocorrem em bancos de dados
# mal planejados ou mal projetados
# Para projetar um banco de dados que evite ter essas anomalias,
# usamos um procedimento chamado normalização
# Em um processo de normalização, aplicamos uma séria de testes
# para verificarmos se uma relação atende a uma forma normal(FN).
# Geralmente, utilizamos as seguintes FNs:
# 1FN -> Primeira forma normal
# 2FN -> Segunda forma normal
# 3FN -> Terceira forma normal

# 1FN
# Usamos a primeira forma normal para eliminar atributos multivalorados
# ou compostos

# Dizemos que uma tabela está na 1FN quando:
	# Possui apenas valores atômicos (indivisíveis)
    # Não há atributos repetidos (apenas 1 dado por coluna)
    # Possui chave primária


CREATE TABLE IF NOT EXISTS usuarios(
		id INT NOT NULL, nome VARCHAR(50) NOT NULL,
        telefone VARCHAR(50) NOT NULL, endereco VARCHAR(200) NOT NULL
);

INSERT INTO usuarios(id, nome, telefone, endereco) VALUES
	(1, "Maria das Dores", "47973651998", "Rua das margaridas, 145"),
    (2, "José Padilha", "47983291009,4789032671", "Rua Ouro, 10"),
    (3, "Rick Fritz", "47823910111", "Avenida 2, 5");

SELECT * FROM usuarios;

# Passando a tabela usuarios para a 1FN
# Adicionando uma chave primária à tabela
ALTER TABLE usuarios ADD PRIMARY KEY(id);

# Removendo os atributos multi valorados da tabela usuarios
CREATE TABLE IF NOT EXISTS telefones(
	id INT NOT NULL PRIMARY KEY AUTO_INCREMENT,
    usuario_id INT NOT NULL,
    telefone VARCHAR(14) NOT NULL,
    FOREIGN KEY(usuario_id) REFERENCES usuarios(id)
);

# Removemos a coluna multi valorada da tabela usuarios
ALTER TABLE usuarios DROP COLUMN telefone;
DESC usuarios;

# 47973651998
# 47983291009,47890326719
# 47823910111

# Inserindo os dados na tabela filha
INSERT INTO telefones(usuario_id, telefone) VALUES
	(1, "47973651998"),
    (2, "47983291009"),
    (2, "47890326719"),
    (3, "47823910111");

SELECT * FROM telefones;

# Mostrando todos os telefones dos usuários
SELECT
	usuarios.id, usuarios.nome,
    telefones.telefone
FROM usuarios
INNER JOIN telefones
	ON usuarios.id = telefones.usuario_id;
    
# Exercicio -> "Quebrar" o campo endereço em outros valores

# 2FN
# Dizemos que uma tabela está na 2FN quando:
	# Ela está na 1FN
    # Cada atributo não chave da tabela for total e funcionalmente
    # dependente de todas as partes da chave primária

CREATE TABLE IF NOT EXISTS tb_fornecedores(
	id INT NOT NULL PRIMARY KEY AUTO_INCREMENT,
    nome VARCHAR(200) NOT NULL
);
    
CREATE TABLE IF NOT EXISTS tb_pecas(
	id INT NOT NULL PRIMARY KEY AUTO_INCREMENT,
    id_fornecedor INT NOT NULL,
    local_fornecedor VARCHAR(100),
    qtd_estoque INT NOT NULL,
    tel_fornecedor VARCHAR(14)
);

ALTER TABLE tb_pecas ADD FOREIGN KEY(id_fornecedor)
REFERENCES tb_fornecedores(id);

ALTER TABLE tb_fornecedores ADD COLUMN local_fornecedor VARCHAR(100);
ALTER TABLE tb_fornecedores ADD COLUMN tel_fornecedor VARCHAR(14);
DESC tb_fornecedores;

ALTER TABLE tb_pecas DROP COLUMN local_fornecedor;
ALTER TABLE tb_pecas DROP COLUMN tel_fornecedor;
DESC tb_pecas;

# 3FN
# Dizemos que uma tabela está na 3FN se:
	# Estiver na 2FN
    # Utilizamos as outras FNs para atingir a 3FN
    # Não existirem dependências transitivas (um atributo não chave
    # ser determinado por outro atributo não chave
    
CREATE TABLE IF NOT EXISTS tb_vendas(
	nota_fiscal INT NOT NULL PRIMARY KEY AUTO_INCREMENT,
    id_vendedor INT NOT NULL,
    nome_vendedor VARCHAR(100) NOT NULL,
    id_produto INT NOT NULL,
    qtd_vendida INT NOT NULL
);

CREATE TABLE IF NOT EXISTS tb_vendedores(
	id INT NOT NULL PRIMARY KEY AUTO_INCREMENT,
    nome VARCHAR(100) NOT NULL
);

ALTER TABLE tb_vendas ADD FOREIGN KEY(id_vendedor)
REFERENCES tb_vendedores(id);

ALTER TABLE tb_vendas DROP COLUMN nome_vendedor;
DESC tb_vendas;
DESC tb_vendedores;

# ---------------------------------------------------------
# TIPOS DE RELACIONAMENTOS
# Um para um -> 1:1
# Um para muitos -> 1:N
# Muitos para muitos -> N:N

# Tabelas para sistema de blog
# Entidades do sistema
# Usuario, Postagem, Comentário, Categorias

CREATE TABLE IF NOT EXISTS tb_usuarios(
	id INT NOT NULL PRIMARY KEY AUTO_INCREMENT,
    login VARCHAR(20) NOT NULL,
    nome VARCHAR(100) NOT NULL
);

# Um usuário faz postagens no blog.
# Ele pode não ter, ter 1 ou várias postagens
# Um post, pode ter apenas 1 autor (usuario)
# id_usuario	| id_post
# 1				| 2
# 1				| 3
# 2				| 5

# Usuário 1 : N Post
# Post 1 : 1 Usuário

CREATE TABLE IF NOT EXISTS tb_postagens(
	id INT NOT NULL PRIMARY KEY AUTO_INCREMENT,
    usuario_id INT NOT NULL,
    titulo VARCHAR(200) NOT NULL,
    mensagem TEXT NOT NULL,
    FOREIGN KEY(usuario_id) REFERENCES tb_usuarios(id)
);


CREATE TABLE IF NOT EXISTS tb_perfis(
	id INT NOT NULL PRIMARY KEY,
    nome VARCHAR(100) NOT NULL,
    sobrenome VARCHAR(100) NOT NULL
);

ALTER TABLE tb_perfis ADD FOREIGN KEY(id) REFERENCES tb_usuarios(id);
DESC tb_perfis;

ALTER TABLE tb_usuarios DROP COLUMN nome;
ALTER TABLE tb_usuarios ADD COLUMN senha VARCHAR(50) NOT NULL;
DESC tb_usuarios;

# Usuario 1 : 1 Perfil
# Perfil 1 : 1 Usuario

INSERT INTO tb_usuarios(login, senha) VALUES
	("agh3415", "123456"),
    ("hpo1214", "abcdef");
    
INSERT INTO tb_perfis(id, nome, sobrenome)
VALUES (1, "Maria", "da Silva");

SELECT
	tb_usuarios.login, tb_perfis.nome,
    tb_perfis.sobrenome
FROM tb_usuarios
INNER JOIN tb_perfis
	ON tb_usuarios.id = tb_perfis.id;
    
    
CREATE TABLE IF NOT EXISTS tb_categorias(
	id INT NOT NULL PRIMARY KEY AUTO_INCREMENT,
    nome VARCHAR(100) NOT NULL
);
DESC tb_categorias;

# Categorias 1 : N Postagens
# Postagem 1 : N Categorias
# N:N -> Muitos para muitos
# Nesse tipo de relação, precisamos criar uma tabela associativa.

# id_postagem	| id_categorias
# 1				| 2
# 1 			| 3
# 1				| 4
# 2				| 7
# 2				| 3

# Tabela associativa tb_postagens_categorias
CREATE TABLE tb_postagens_categorias(
	id_postagem INT,
    id_categoria INT,
    PRIMARY KEY(id_postagem, id_categoria),
    FOREIGN KEY(id_postagem) REFERENCES tb_postagens(id),
    FOREIGN KEY(id_categoria) REFERENCES tb_categorias(id)
);
DESC tb_postagens_categorias;