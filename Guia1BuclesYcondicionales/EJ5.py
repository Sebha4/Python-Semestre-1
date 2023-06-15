import random

numeros = [random.randint(40, 350) for _ in range(20)]

print("numeros generados:")
print(numeros)

numero_buscado = int(input("de los numeros generados, elije uno: "))

ocurrencias = numeros.count(numero_buscado)


print(f"El número {numero_buscado} sale {ocurrencias} veces en la lista.")