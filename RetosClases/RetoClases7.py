def obtener_longitudes_palabras(frase):
    longitudes = {}
    palabras = frase.split()

    for palabra in palabras:
        longitudes[palabra] = len(palabra)

    return longitudes


frase = input("Ingresa una frase: ")
resultados = obtener_longitudes_palabras(frase)
print(resultados)
