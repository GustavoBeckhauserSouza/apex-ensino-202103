
# break -> Interrompe a execução do laço

if __name__ == '__main__':
    lista_de_compras = [
        "Banana", "Manga", "limão", "Morango",
        "hoje", "Melancia", "Caqui"
    ]

    for item in lista_de_compras:
        if item == "hoje":
            break
        print(item)
