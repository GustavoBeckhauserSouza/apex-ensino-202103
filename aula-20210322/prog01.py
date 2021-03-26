"""
Lógica de programação

- Entrada e saída
- Tipos de dados (string e números)
- Laços de condição
"""

if __name__ == '__main__':
    # print() imprime algo no terminal
    print("Hello world.")

    # input() recebe uma entrada pelo terminal.
    # Depois, atribuímos o valor retornado pela função input() a variável nome
    # nome = input("Digite o seu nome: ")
    # print(nome)

    # tipo de dado string
    # Receber o nome e a idade do usuário, e imprimir no seguinte formato:
    # Olá <usuario>, você tem <idade> anos.
    nome = input("Digite o seu nome: ")
    idade = input("Digite a sua idade: ")

    # Concatenando as string
    print("Olá " + nome + ", você tem " + idade + "anos.")

    # Substituindo o valor pelo marcador %s
    print("Olá %s, você tem %s anos" % (nome, idade))

    # Usando o método de string format()
    print("Olá {}, você tem {} anos.".format(nome, idade))

    # f-strings
    print(f"Olá {nome}, você tem {idade} anos.")