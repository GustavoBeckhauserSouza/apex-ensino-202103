
def calculo_salario(nome, valor, setor, horas_trabalhadas=0, porcentagem_comissao=0):

    print(f"Cálculo do salário de {nome}")

    if setor == 1:
        print(f"Valor: {valor}")

    elif setor == 2:
        print(f"Quantidade de horas trabalhadas: {horas_trabalhadas}")
        print(f"Valor da hora trabalhada: {valor}")
        print(f"Valor: {valor * horas_trabalhadas}")

    elif setor == 3:
        print(f"Valor das vendas: {valor}")
        print(f"Porcentagem de comissão: {porcentagem_comissao}")
        print(f"Valor da comissão: {valor * (porcentagem_comissao / 100)}")


if __name__ == '__main__':

    nome = input("Digite o seu nome: ")
    valor = float(input("Digite o valor: "))
    setor = int(input("Digite o setor: "))

    if setor == 1:
        calculo_salario(nome, valor, setor)

    if setor == 2:
        qtd_horas = int(input("Informe a quantidade de horas trabalhadas: "))
        calculo_salario(nome, valor, setor, horas_trabalhadas=qtd_horas)

    if setor == 3:
        porcentagem_comissao = int(input("Informe a porcentagem de comissão"))
        calculo_salario(nome, valor, setor, porcentagem_comissao=porcentagem_comissao)
