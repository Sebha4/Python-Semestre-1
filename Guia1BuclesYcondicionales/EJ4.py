n = int(input("num cubos: "))

impares = 1
suma_impares = 0

for i in range(n):
    suma_impares += impares
    cubo = suma_impares ** 3
    print(f"{i+1}: {suma_impares} = {cubo}")
    impares += 2


