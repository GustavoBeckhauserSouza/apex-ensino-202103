"""
Faça um programa que peça o nome e o valor de um produto. Se o valor
do produto for menor que 100 reais, não dê desconto.
Se o valor do produto for menor que 1000 reais e maior ou igual a 100
reais, dê um desconto de 5%.
Se o valor do produto for maior ou igual a 1000 reais, de um desconto
de 10%.
Exemplo:

Informe o nome do produto:
Informe o valor do produto:

Produto: Ar-condicionado
Valor: 1500
Desconto aplicado: 10%
Valor com desconto: 1350
"""

if __name__ == '__main__':
    nome_produto = input("Informe o nome do produto: ")
    valor_produto = float(input("Informe o valor do produto: "))

    if valor_produto < 100:
        valor_desconto = 0
    elif valor_produto >= 100 and valor_produto < 1000:
        valor_desconto = 0.05
    else:
        valor_desconto = 0.1

    valor_final = valor_produto - (valor_produto * valor_desconto)

    # print("Produto: " + nome_produto)
    # print("Produto {}".format(nome_produto))
    print(f"Produto: R$ {nome_produto}")
    print(f"Valor: {valor_produto}")
    print(f"Desconto aplicado: {int(valor_desconto * 100)}%")
    print(f"Valor com desconto: {valor_final}")