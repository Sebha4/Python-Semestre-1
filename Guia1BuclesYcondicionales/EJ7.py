def facto(x):
    if x == 0:
        return 1
    elif x >= 1:
        return x * facto(x - 1)

numero = int(input("Ingrese un numero: "))

resultado = facto(numero)

print(f"El facto de {numero} es: {resultado}")
