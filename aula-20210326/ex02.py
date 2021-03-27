"""
Exercício 02

Criar uma função que calcule o IMC de uma pessoa e retorne o valor.
A fórmula de cálculo é a seguinte:

imc = peso / (altura * altura)
peso deve ser descrito em Kgs       (ex. 85.5)
altura deve ser descrita em metros  (ex. 1.76)

"""


def ex02(peso, altura):
    return peso / (altura * altura)


if __name__ == '__main__':
    peso = float(input("Informe o peso(Kgs): "))
    altura = float(input("Informe a altura(Mts): "))

    imc = ex02(peso, altura)

    print("Seu IMC é de {:.2f}".format(imc))