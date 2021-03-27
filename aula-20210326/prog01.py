"""
Funções

Função é um bloco de código que é executado quando é chamado, e pode
ser reaproveitado em qualquer parte do código. O uso de funções
facilita o reuso de código dentro da nossa aplicação, assim como uma
maior modularidade.

Sintaxe:
def <nome_da_funcao>([argumentos]):
    <bloco_de_codigo>
    [return]

"""


def mostrar_mensagem_boas_vindas():
    print("Seja bem-vindo")

# Uma função pode receber um ou mais argumentos(ou parâmetros)
# Dessa maneiro, somos obrigados a passar o argumento nome
def mostrar_mensagem_usuario(nome):
    print(f"{nome}, você entrou no sistema.")


# Os argumentos de uma função são sempre separados por vírgula
def soma(numero1, numero2):
    print(f'{numero1 + numero2}')


# Argumentos obrigatórios devem ser informados na ordem correta
def divisao(numero1, numero2):
    print(f'{numero1 / numero2}')


# Podemos definir um valor padrão para qualquer argumento da função
def repete_texto(texto, numero_de_vezes=20):
    print(f"{texto*numero_de_vezes}")


# return retorna o valor de uma função
def media_tres_numeros(numero1, numero2, numero3):
    media = (numero1 + numero2 + numero3) / 3
    return media


# Uma lista recebe qualquer tipo de valor pelo argumento
def imprimir_valores(lista_de_valores):
    for valor in lista_de_valores:
        print(valor)


if __name__ == '__main__':
    mostrar_mensagem_boas_vindas()
    mostrar_mensagem_usuario("Alessandro")
    soma(4, 7)
    divisao(0, 4)

    # Usando o nome dos argumentos (keywords), não precisamos respeitar a ordem
    repete_texto(numero_de_vezes=10, texto="#")
    repete_texto('*')
    print(soma(10, 10))
    media = media_tres_numeros(6, 7, 8)
    print(media)
    imprimir_valores([10, 20, 30, 40, 50])