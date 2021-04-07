
def intervalo(numero, inicio_intervalo, fim_intervalo):
    return numero >= inicio_intervalo and numero <= fim_intervalo


if __name__ == '__main__':
    numero = int(input("Informe o número: "))
    inicio_intervalo = int(input("Informe o início do intervalo: "))
    fim_intervalo = int(input("Informe o fim do intervalo: "))

    mensagem = f"{numero} está entre {inicio_intervalo} e {fim_intervalo}? " \
               f"{intervalo(numero, inicio_intervalo, fim_intervalo)}"

    print(mensagem)
