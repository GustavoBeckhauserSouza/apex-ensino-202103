
def celsius_para_fahrenheit(temperatura):
    valor = temperatura * (9 / 5) + 32
    return valor


def fahrenheit_para_celsius(temperatura):
    valor = (temperatura - 32) * (5 / 9)
    return valor


if __name__ == '__main__':

    temperatura = float(input("Informe a temperatura: "))
    mensagem = """
    Informe o código de conversão
    1) Celsius -> Fahrenheit
    2) Fahrenheit -> Celsius
    """
    print(mensagem)
    codigo = int(input("Informe o código: "))

    if codigo == 1:
        resultado = celsius_para_fahrenheit(temperatura)
        print(f"{temperatura}ºC corresponde a {resultado}ºF")
    elif codigo == 2:
        resultado = fahrenheit_para_celsius(temperatura)
        print(f"{temperatura}ºF corresponde a {resultado}ºC")
    else:
        print("Código inválido")