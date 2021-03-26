
# continue -> Volta ao início da execução do laço for, para o proximo
# item

if __name__ == '__main__':
    lista_de_numeros = [
        1, 2, 3, 4, 5, 6, 7, 8, 9, 10
    ]

    for numero in lista_de_numeros:
        if numero % 2 == 1:
            continue

        print(numero ** 2)