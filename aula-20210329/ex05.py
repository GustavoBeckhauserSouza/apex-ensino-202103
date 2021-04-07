

def retorna_numeros_pares(lista):
    lista_final = []

    for numero in lista:
        if numero % 2 == 0:
            lista_final.append(numero)

    return lista_final


if __name__ == '__main__':

    lista_numeros = [2, 3, 6, 7, 10, 15, 121, 124, 200]
    retorno = retorna_numeros_pares(lista_numeros)
    print(retorno)

    # Se formos inserir a lista diretamente pelo terminal, podemos seguir
    # algumas abordagens
    # entrada_numeros = input("Informe uma lista de números separada por virgula")

    # List Comprehension
    # entrada_numeros = entrada_numeros.split(',')
    # entrada_numeros = [int(item) for item in entrada_numeros]

    # A segunda é percorrer a string convertendo o que é caractere numérico
    # para int e salvando em uma segunda lista
    # lista_numeros = []
    # for numero in entrada_numeros:
    #     if numero.isdigit():
    #         lista_numeros.append(int(numero))