#Operadores MATEMATICOS
print("Suma en a y b:", a + b)
print ("Un modulo entre:", a % b)

#declaranto variables tipo flotantes

t= 5.39# Tiempo en segundos
g= 9.81# La aceleracion de la gravedad


#Operaciones aritmeticas con flotantes

v = g + t

print (f"La velocidad del objeto en caida libre es de": {v}, e\s)
print ("La velocidad de caida libre es de: {:,2f}" , format(v))
print ("La velocidad de caida libre es de": {v:,2f})
print ("la velocidad del objeto de caida libre es de: "v:2f")

#Declarando variables de tipo complejo
c1 = 4 + 3j
print (type(c1))

#Creando un numero complejo con complex
c2 = complex (3, -5)
print("El numero complejo es de :", c2)

Print(c2.real)# Conocinedo la parte real del numero complejo
print (c2,imag) #Conocinedo la parte imaginario del numero complejo

print ("Hola" * 5)

#02 Comparando cadenas de caracteres
animal_domestico = "gato"
animal_salvaje= "Leopardo"
print("\Comparando Cadena de caracteres")
print(animal_domestico == animal_salvaje) #igual a
print(animal_domestico != animal_salvaje) desigual a
print(animal_domestico > animal_salvaje) #Mayor que
print(animal_domestico < animal_salvaje) #menor que
print(animal_domestico <= animal_salvaje) #Menor o igual que
print(animal_domestico >= animal_salvaje) #Mayor o igual que

#03 Operadores Logicos

bencina = True
encendido = True
edad = 19

#Utilizando el operador AND
if bencina and encendido;
    print("El vechiculo puede avanzar")
else:
    print("El vehiculo no puede avanzar")

#utilizando el operador OR
print 
if bencina or encendido:
    print("El vehiculo puede avanzar")
else:
    print("El vehiculo no puede avanzar")

#Utilizando el NOT junto al OR
if not bencina or encendido:
    print("el vehiculo puede avanzar")
else:
    print("El vehiculo no puede avanzar")

    #Utilizando el NOT junto al AND
if not bencina and encendido:
    print(Utilizando el NOT y AND "el vehiculo puede avanzar")
else:
    print("El vehiculo no puede avanzar")


#Utilizando el NOT, OR y AND Juntos
if not bencina or (encendido and edad >= 18):
    print("el vehiculo puede avanzar")
else:
    print("El vehiculo no puede avanzar")


#USO DE WHILE
edad = 15
num = 0
while edad < 10:
print("Eres menor de edad, no puedes manejar poruqe tienes",edad)
edad= +1 

#Que hace este bucle?
while num <= 100:
print(num)
num += 1
while edad <= 10

#Combinando white y else
while num <= 100:
print(num)
num += 2
#num = num + 2
print ("Primer bucle terminado\n")

#La funcion isdigit Solo permite trabajar con digitos y no con caracteres
while not edad.isdigit() and int(edad) < 0:

#La funcion forwar puede servir para enumerar opciones, Paciente[1] Paciente[2] Paciente[3]

peso = float (input) "Ingrese el peso del paciente {} (kg):" , format(i+1))





