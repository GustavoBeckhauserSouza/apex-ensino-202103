
# Laço while: É executado enquanto uma condição
# for verdadeira

if __name__ == '__main__':
    lista_de_numeros = []

    comando = None  # None -> Valor nulo

    while comando != "SAIR":
        comando = input("Informe o valor: ")

        if not comando.isdigit():
            continue

        # O método append() insere um novo item
        # no final da lista
        lista_de_numeros.append(int(comando))

    print(sum(lista_de_numeros))
    print(lista_de_numeros)

    soma = 0

    for numero in lista_de_numeros:
        # soma = soma + numero
        soma += numero

    print(soma)