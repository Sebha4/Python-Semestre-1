a = [10, 80, 15, 30, 20]
b = [20, 45, 80, 20, 10]
c = [20, 35, 60, 90, 20]

#1

def valores_comun(lista1, lista2, lista3):
    return list(set(lista1) & set(lista2) & set(lista3))

valores_comunes = valores_comun(a, b, c)
print("Los valores en común de las tres listas son:", valores_comunes)

#2
def concatenar_listas(*listas):
    resultado = []
    for lista in listas:
        resultado.extend(lista)
    return resultado



concatenada = concatenar_listas(a, b, c)
print("Lista concatenada:", concatenada)


3#
def eliminardupli(lista):
    return list(set(lista))

sin_duplicados = eliminardupli(concatenada)
print("Lista sin duplicados:", sin_duplicados)

#5
def ordenardescendente(lista):
    return sorted(lista, reverse=True)

ordenada = ordenardescendente(sin_duplicados)
print("Lista ordenada de forma descendente:", ordenada)

#5
def reemplazar(lista, valor, posicion):
    lista[posicion] = valor
    return lista

print("Lista con valor reemplazado:")
