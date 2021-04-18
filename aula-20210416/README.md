# Módulo Python

## Introdução

Python é definida como uma linguagem interpretada, de alto nível e de propósito geral. Além disso, é dinamicamente tipada que suporta múltiplos paradigmas de programação, como o procedural, orientado a objetos e funcional.

## Regras de sintaxe

1. A Linguagem Python é **case sensitive**. Python distingue letras maiúsculas de minúsculas. Por exemplo, a variável nome_funcionario é diferente de Nome_funcionario:

    ````python
    nome_funcionario = "Joana"

    print(Nome_funcionario) # essa linha gerará uma exceção.
    ````

2. Não usamos `;` ou qualquer outro caractere para indicar o término de um comando. O próprio fim da linha indica que o comando terminou:
    ````python
    print("Olá")
    print("Esse é o próximo comando")
    ````

3. Caso queiramos digitar mais de um comando por linha no Python, devemos utilizar o `;` para separar os comandos:
    ````python
    nome = "Luiz"; print(nome)
    ````

4. Podemos usar aspas simples `''`, aspas duplas `""` e aspas triplas `''' ou """` para representarmos strings:
    ````python
    nome = 'José'
    frase = "Olá mundo"
    texto = """
        Primeira sentença
        Segunda sentença
    """
    ````

5. Utilizamos o caractere `#` para definir um comentário:
    ````python
    # O comando abaixo gera uma lista de inteiros de 1 a 10
    lista_numeros = [numero for numero in range(1, 11)]
    ````

6. Se quisermos definir um comando multilinha, usamos o caractere `\`. Expressões dentro de `()`, `[]` ou `{}` não precisam desse caractere especial:
    ````python
    itens = [
        'Espada', 'Escudo', 'Mapa',
        'Cantil', 'Poção de cura'
    ]

    calculo = 4 + 5 * \
        (4 ** 3) - (10 / 2) \
        (3 + 2)
    ````

7. Python usa fortemente a identação de código em suas regras de sintaxe. Linguagens como Java, C++ ou C# usam `{}` para definir blocos de código, por exemplo:
    ````Java
    int dividir(num1, num2) {
        if (num2 == 0) {
            throw new Exception("O divisor não pode ser 0!");
        }

        return num1 / num2;
    }
    ````

    porém, diferentemente dessas, Python usa identação para separar seus blocos de código. De acordo com a PEP-8 (uma espécie de guia de boas práticas para o código Python), devemos usar a identação de 4 espaços. A identação dentro de um bloco de código para as instruções deve ser a mesma:
    ````python
    if usuario == "Maria":
    print("Maria logada")
    # O print acima não está sendo considerado como dentro do if, logo essa instrução causará um erro de sintaxe

    if usuario == "João":
        print("João logado")
        # A linha acima está ok usando uma identação de 4 espaços com relação a linha acima

          print("Bem-vindo")
          # Essa linha causará erro, pois temos uma identação de 6 espaços, diferente da última instrução

        print("Preparando ambiente")
        # Essa linha não causará erros, pois tem a mesma identação da primeira instrução
    ````

    Definimos um bloco de código depois que usamos
    o caractere `:` nos casos:
    ````python
    # Cláusula if... elif... else
    if condition:
        pass
    elif else_condition:
        pass
    else:
        pass

    # Definição de funções
    def function():
        pass

    # Definição de classes
    class User:

        # Definição dos métodos de uma classe
        def method_read():
            pass

    # Criação de contextos com with
    with open("file.txt") as _file:
        pass

    # laços for e while
    for number in range(1, 10):
        pass

    while condition:
        pass

# Exercícios
1. Escreva um programa que conte quantas linhas existem em um arquivo .txt (arquivo.txt)
2. Escreva um programa que vai receber nomes até o usuário digitar "sair". Então o programa vai pedir o diretório onde o usuário deseja salvar o arquivo. O programa vai salvar esses nomes em um arquivo .txt dentro do diretório escolhido
3. Escreva um programa que leia um arquivo CSV e imprima o nome das colunas, depois todos os registros (pedidos.csv)
4. Escreva um programa que receba via terminal os registros de uma compra (codigo, nome e valor). E salve esses registros em um arquivo .csv.
5. Escreva um programa que leia um arquivo csv de registro de pedidos. Ao final, o programa mostrará a quantidade total de pedidos, o valor total e a data/hora do último pedido (pedidos.csv)
6. Escreva um programa que receba, via terminal, uma data qualquer. O programa vai mostrar os registros de um arquivo csv apenas daquela data. (pedidos.csv)