def ingresanombres():
    nombres = []
    while True:
        nombre = input("Ingrese un nombre (o escriba 'finalizar' para finalizar la lista): ")
        if nombre == 'finalizar':
            break
        nombres.append(nombre)
    return nombres

def contletras(nombres):
    total_letras = 0
    for nombre in nombres:
        total_letras += len(nombre)
    return total_letras
nombres = ingresanombres()
total_letras = contletras(nombres)


def imprimirResultados(nombres, total_letras):
    print("Nombres ingresados:")
    for nombre in nombres:
        print(nombre)
    print("Total de letras contadas:", total_letras)

nombres = ingresanombres()
total_letras = contletras(nombres)
imprimirResultados(nombres, total_letras)
