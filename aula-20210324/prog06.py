"""
Desenvolva um programa de lista de compras. O programa vai pedir
novos itens a serem adicionados na lista até o usuário digitar
"PRONTO". Após isso, serão mostrados todos os itens da lista,
linha por linha.

Digite o item: Banana
Digite o item: Maçã
Digite o item: Manga
Digite o item: PRONTO

== ITENS DA LISTA DE COMPRAS ==
Banana
Maçã
Manga

"""

if __name__ == '__main__':
    lista_de_compras = []

    item = ""

    # O método upper() transforma todas os caracteres em maiúsculo.
    while item.upper() != "PRONTO":
        item = input("Digite o item: ")

        lista_de_compras.append(item)

    # O método pop() remove e retorna o último item inserido na lista
    # Se for passado o índice, remove o item no índice informado
    lista_de_compras.pop()

    print("*"*30)
    for item in lista_de_compras:
        print(f"* {item}")