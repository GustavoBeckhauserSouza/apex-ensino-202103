"""
Dicionários

Um dicionário é um tipo de dado em Python que é definido como uma
estrutura do tipo chave: valor. As chaves nunca podem ser repetidas
dentro do dicionário, os valores sim. Outra característica é que
as chaves devem ser do tipo string ou numérico. Já os valores
podem ser de qualquer tipo, inclusive outro dicionário.

"""


if __name__ == '__main__':
    # Exemplo de dicionário
    funcionario_paulo = {
        "nome": "Paulo",
        "setor": 3,
        "valor": 12589.23,
        "porcentagem_comissao": 20,
        "valor_salario": 2517.85,
        "dados_admissao": {
            "data_inicio": "1998-03-07",
            "data_fim": ""
        },
        "premios": [
            "Melhor vendedor 1999",
            "Funcionário do ano 2002",
        ]
    }

    # Devemos usar a sintaxe dicionario['chave'] para acessar um
    # valor dentro desse dicionário
    print(f"Nome do funcionário: {funcionario_paulo['nome']}")

    # Caso coloquemos um nome errado de chave, receberemos uma exceção KeyError
    # print(f"Salário do funcionário: {funcionario_paulo['valor_salrio']}")

    # Podemos usar o método get() para nos assegurarmos de não causar uma exceção KeyError
    # caso a chave do dicionário não exista. Também podemos definir um valor padrão caso
    # isso aconteça.
    print(f"Cargo do funcionário: {funcionario_paulo.get('cargo', 'Cargo não definido')}")


    # Como um dicionário é um tipo iterável, podemos percorrer as chaves e/os valores
    # utilizando o laço for

    # Utilizando o laço for no dicionário diretamente
    # Tem o mesmo efeito se utilizássemos funcionario_paulo.keys()
    # Aqui listamos todas as chaves do dicionário
    for item in funcionario_paulo:
        print(item)

    # Utilizamos o método values() para listar os valores do dicionário
    for item in funcionario_paulo.values():
        print(item)

    # Quando queremos listar tanto as chaves quanto os valores, utilizamos o método items()
    for chave, valor in funcionario_paulo.items():
        # isinstance() verifica se um valor é uma instância de um tipo
        if isinstance(valor, list):
            print(f"{chave}")
            for item in valor:
                print(f"* {item}")
            continue
        else:
            print(f"{chave}: {valor}")
