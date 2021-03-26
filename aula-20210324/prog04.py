
# else -> É executado todas as vezes que o laço termina

if __name__ == '__main__':
    lista_de_numeros = [
        1, 2, 3, 4, 5, 6, 7, 8, 9, 10
    ]

    for numero in []:
        if numero % 2 == 1:
            continue

        print(numero ** 2)

    # É executado independentemente de o bloco for ter sido executado
    # ou não
    else:
        print("Quadrados calculados.")