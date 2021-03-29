"""
Dicionários

Um dicionário é um tipo de dado em Python que é definido como uma
estrutura do tipo chave: valor. As chaves nunca podem ser repetidas
dentro do dicionário, os valores sim. Outra característica é que
as chaves devem ser do tipo string ou numérico. Já os valores
podem ser de qualquer tipo, inclusive outro dicionário.

"""

if __name__ == '__main__':
    produto01 = {
        'nome': 'Salame',
        'preco': 19.90,
        'peso': 0.600
    }

    # Para alterar um valor associado a uma chave no dicionário,
    # podemos fazê-lo diretamente.
    produto01['preco'] = 21.10

    # print(produto01)

    # Podemos usar o método update() para atualizar os valores do dicionário. Se quaisquer
    # chaves indicadas no argumento do update não existirem, elas serão criadas.
    produto01.update({'preco': 22, 'validade': '2021-12-12'})

    print(produto01)

    # O método pop() exclui o elemento informado no argumento a partir da chave informada.
    produto01.pop('validade')

    print(produto01)