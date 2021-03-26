"""
Estruturas de repetição em Python
Executam um bloco de código enquanto uma condição
for verdadeira ou enquanto existirem items em uma
sequência. Para isso, utilizamos as seguintes
palavras reservadas:

- for
- while

for: Itera(percorre) sobre uma sequência enquanto existirem
itens nessa sequência

"""

if __name__ == '__main__':
    # palavra = "Python"

    # Listas em Python
    # Uma lista em Python pode armazenar qualquer tipo de valor
    # lista_de_compras = list("Banana")
    lista_de_compras = ["Banana", "Abacate", "Maçã", 10, [1, 2, 3]]

    for item in lista_de_compras:
        print(item)
