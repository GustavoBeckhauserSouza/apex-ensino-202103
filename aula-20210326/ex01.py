"""
Exercício 01

Escreva uma função que receba uma lista de 5 números, e retorne
outra lista com os quadrados de cada número.

lista de entrada: [2, 4, 5, 6, 8]
lista de saída: [4, 16, 25, 36, 64]

def ex01(lista):
    pass

print(ex01([2, 4, 5, 6, 8]))

"""


def ex01(lista):
    lista_quadrados = []
    for item in lista:
        quadrado = item * item
        lista_quadrados.append(quadrado)

    return lista_quadrados


if __name__ == '__main__':
    print(ex01([2, 4, 5, 6, 8]))
    print(ex01([1, 7, 11, 15, 90]))