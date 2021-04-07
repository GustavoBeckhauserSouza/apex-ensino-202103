from ex05 import retorna_numeros_pares

def exclui_repetidos(lista_numeros):
    lista_nao_repetidos = []

    for numero in lista_numeros:
        if numero not in lista_nao_repetidos:
            lista_nao_repetidos.append(numero)

    return lista_nao_repetidos

if __name__ == '__main__':
    lista_numeros = [1, 1, 2, 4, 5, 7, 7, 7, 8, 9, 9, 9, 10]
    lista_final = exclui_repetidos(lista_numeros)
    print(lista_final)
    print(retorna_numeros_pares())

    # Poderíamos fazer a mesma coisa convertendo a lista para um set,
    # e depois convertendo novamente para lista
    # print(list(set(lista_numeros)))
