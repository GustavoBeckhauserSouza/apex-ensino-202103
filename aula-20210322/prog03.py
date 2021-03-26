# Booleano (boolean)
# True, False


if __name__ == '__main__':

    # True -> Verdadeiro
    # False -> Falso
    # print(True)

    numero1 = float(input("Digite o primeiro número: "))
    numero2 = float(input("Digite o segundo número: "))

    # Isolamos a soma utilizando parentesis
    media = (numero1 + numero2) / 2

    print(f"Média: {media}")

    # Estrutura de condição if... elif... else
    # Operadores de comparação
    # > Maior que
    # < Menor que
    # == Igual a
    # >= Maior ou igual a
    # <= Menor ou igual a
    # != Diferente

    # Se a média for igual ou maior que 7, imprimir ("Você passou")

    # Sempre temos que usar dois pontos quando usamos estruturas de controle
    # de condição, repetição, classes, funções, etc.
    if media >= 7:
        print("Você passou")
    elif media >= 5 and media < 7: # else if
        print("Você está de recuperação.")
    else:
        print("Você foi reprovado")
