

def contar_maiuscular_minusculas(texto):
    info = {
        "maiusculas": 0, "minusculas": 0
    }

    for letra in texto:
        if letra.isupper():
            # info['maiusculas'] = info['maiusculas'] + 1
            info['maiusculas'] += 1
        elif letra.islower():
            info['minusculas'] += 1

    return info


if __name__ == '__main__':
    texto = input("Digite um texto qualquer: ")
    print(contar_maiuscular_minusculas(texto))