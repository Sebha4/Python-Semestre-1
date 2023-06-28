print("Hola Mundo")
#Declarando una variable
nombre = "Sebastián"
name="Sebastián"
print(name)
print("Hola mundo" ,nombre)
#declaramos la edad
edad= 18
print(edad)
#imprimimos 2 variables en una misma sentencia


#04-IMPRIMIENDO 2 VARIABLES EN UNA MISMA LINEA 
#(concatenación con signo +, utilizando comas y Formato cadenas literales)
#print("Hola mi nombre es" + nombre + "y tengo" + edad + "años") #Esta sentencia da error ¿por qué?

print('Hola mi nombre es',nombre,"y tengo",edad) #Impresion separando con comas
print("Hola mi nombre es"+" "+name+" "+"y tengo"+str(edad)) #Concatenación con signo +
print(f"Hola mi nombre es {nombre} y tengo {edad} años") #Formato de cadenas literales (f-string)


print("Hola, mi nombre es " + nombre + " Y tengo " + str(edad)  +" años ")
#Actualizando la variable nombre
print("Hola, mi nuevo nombre es")
print("Hola esta es una prueba para ver si la pagina se actualiza")



#08-ACOTACIÓN CONSTANTES
'''En Python no existen las constantes, por convención se identifican y se declaran con mayusculas
como se muestra a continuación'''
PI = 3.14
CIUDAD = "Osorno"