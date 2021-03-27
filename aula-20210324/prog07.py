"""
Escreva um programa que receba 3 nomes e 3 sobrenomes e os armazene
em listas diferentes.
Após isso, imprima na tela, linha por linha, todas as combinações de
nomes e sobrenomes. Por exemplo

Digite o nome: João
Digite o nome: Maria
Digite o nome: Luana

Digite o sobrenome: Silva
Digite o sobrenome: Cardozo
Digite o sobrenome: Bezerra

João Silva
João Cardozo
João Bezerra

Maria Silva
Maria Cardozo
Maria Bezerra

Luana Silva
Luana Cardozo
Luana Bezerra

Utilizar o conceito de "for encadeado"

"""


if __name__ == '__main__':
    lista_de_nomes = []
    lista_de_sobrenomes = []

    # A variável contador vai controlar a quantidade de registros
    # que vamos receber pelo terminal
    contador = 0

    # Enquanto o valor de contador for menor que 3, ele adiciona a
    # lista de nomes o novo nome
    while contador < 3:
        nome = input("Digite um nome: ")
        lista_de_nomes.append(nome)
        contador = contador + 1

    # o built-in range() gera uma sequência de números, iniciando
    # no 0.
    # range(3) -> 0, 1, 2
    # range(5) -> 0, 1, 2, 3, 4
    # range(1, 6) -> 1, 2, 3, 4, 5
    for i in range(3):
        sobrenome = input("Digite o seu sobrenome: ")
        lista_de_sobrenomes.append(sobrenome)

    # Utilizaremos um for encadeado, ou seja, um for após o outro
    for nome in lista_de_nomes:
        for sobrenome in lista_de_sobrenomes:
            print(f"{nome} {sobrenome}")
