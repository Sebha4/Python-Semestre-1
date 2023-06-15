def numeros():
    numeros = []
    while True:
        numero = int(input("Ingrese un número:\n> "))
        if numero == -1:
            break
        elif numero > 0:
            numeros.append(numero)
    return numeros

def calcular_mayor(numeros):
    return max(numeros)

def calcular_sumatoria(numeros):
    return sum(numeros)

def calcular_sumatoria_pares(numeros):
    pares = [numero for numero in numeros if numero % 2 == 0]
    return sum(pares)

def calcular_sumatoria_impares(numeros):
    impares = [numero for numero in numeros if numero % 2 != 0]
    return sum(impares)

def calcular_promedio(numeros):
    return sum(numeros) / len(numeros)

numeros_ingresados = numeros()
mayor = calcular_mayor(numeros_ingresados)
sumatoria_total = calcular_sumatoria(numeros_ingresados)
sumatoria_pares = calcular_sumatoria_pares(numeros_ingresados)
sumatoria_impares = calcular_sumatoria_impares(numeros_ingresados)
promedio = calcular_promedio(numeros_ingresados)

print("Número mayor:", mayor)
print("Sumatoria total:", sumatoria_total)
print("Sumatoria de números pares:", sumatoria_pares)
print("Sumatoria de números impares:", sumatoria_impares)
print("Promedio:", promedio)

if mayor > promedio:
    print("El número mayor es mayor que el promedio y este es ", mayor)
elif mayor < promedio:
    print("El número mayor es menor que el promedio y este es.", mayor)
else:
    print("El número mayor es igual al promedio.", mayor)