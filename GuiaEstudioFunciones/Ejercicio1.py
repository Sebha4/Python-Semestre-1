import random
numeros=int(input("Ingrese la cantidad de numeros que quiere generar: "))
numerosGenerados= [random.randint(0, 1000) for _ in range(numeros)]
print("Estos son los numeros generados:", numerosGenerados)

#La suma de todos los numeros
suma_Todoslosnumeros= sum(numerosGenerados)
print(suma_Todoslosnumeros)

#Suma de los numeros pares
numero_par= numerosGenerados

suma_pares = sum(numero_par for numero_par in numero_par if numero_par % 2 != 1)

print("La suma de los números impares de la lista es:", suma_pares)


#La suma de los numeros impares
numero_impar= numerosGenerados

suma_impares = sum(numero_impar for numero_impar in numero_impar if numero_impar % 2 != 0)

print("La suma de los números impares de la lista es:", suma_impares)







