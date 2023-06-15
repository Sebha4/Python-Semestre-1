#Principales funciones del lenguaje de programación
str
int
float
len
count()

#01 DATOS DE TIPO NUMERICO

estatura = 1.71
peso = 70
complejo = 1 + 4j

print("Transformando valor real a entero:",int(peso))
print("Transformando valor entero a real",int(peso))

print("Impresion del numero complejo: ", complejo)
inc= peso/estatura**2
print(inc)

#02Valores de tipo cadena de caracteres
asignatura = "Programación"
carrera = "Ingenieria civil en informatica"

print("La asignatura de", )

#03 VALORES BOOLEANOS
ampolleta = False
interruptor = True

#Con type sabemos el tipo de datos que estamos tratando
print(type(ampolleta))

#04DATOS TIPOS ARRAY (Objetos de tipo Colección)
estudiantes =("Matias", "Marco", "Cristobal", "Sebastián")
num = [1,2,3,4,5,6]
print(estudiantes)
print(num)

#05Declaración de variables en una sola linea

ciudad, region, pais, year ="Puerto Montt, Los Lagos, Chile, 2020"

#¿Se puede realizar una lista de datos compuestos?


#06declarando listas
estudiantes=[Sebastián,Jose,Matias,Pedro]
#Para buscar una variable de una lista
print(estudiantes.count("Marco"))#Cantidad de elementos de una lista

lenguaje= ["JavaScript"]
print("Nuevo valor del arreglo de un elemento:", lenguaje)

#Entrar a una list o declarar list 
Print (f"La estatura de los alumnos está en [Estatura]") #Se usa las llaves para darle a enteder al programa que de esta forma se entra a una lista de variables

#Operacion matematica basica
imc = peso / (Estatura**2)
print(f"Mi IMC es de: [imc]\n")

#Valores BOLEANOS
ampolleta = False
Interructor = True

Print ("La variable ampolleta es de tipo" ,type(Interructor),"\n"

#Podemos tranformar cualquier valor a boleano
print(bool(0))      
print(bool("")) 
print(bool(none))  
print(bool(1))
print(bool("False"))
print(bool("\n"))

#Se pueden guardar listas de esta manera
list([1,2,3,4,5])
#Como tambien de esta manera que es mas eficiente
numeros= [1,2,3,4,5]

#Como se pido la lista?
print("Lista de numeros":,list)
#Para contar la cantidad de veces de una letra en una lista se usa "Count"
print(estudiantes:count("Marco"))
#Como accedo a un elemento especifico de la lista tipo numerio?
print(estudiantes[0])#Siempre se cuenta a partir del 0 en programación
print(estudiantes[-1])#En el caso de que sean numeros negativos.


#Inicializando otra lista de datos mixtos
data_asig = [10023,"Programación", 1,True]
#¿Que hace este codigo?
cod,ramo,semestre,estado = data_asing
print (ramo)
#Se puede crear una lista con estos datos compuestos?

#¿Que hacen estás funciones?
print(list("Python"))
print(list(range(10.23)))
print("\n")

#El index me muestra la pocicion en laque se encuentra un elemento en la lista

#07 DICCIONARIO
print ("######## 07 DICCIONARIO ######")

diccionario = dict()
diccionario = {}

#Suele funcionar como mapas, como clave de valor

Datos_personales = {
    "Nombre":"Victor",
    "Instituciin":"Ulagos",
    "Edad": 29,
    "asignatura": ("Estructura de datos", "Programacion")
}

#Quiero consultar la cantidad de elementos del diccionario
print(len(Datos_personales))

#Como actualizar un elemento dentro del diccionario
Datos_personales["Institucion"] ="USS"
print ("Diccionario actualizado:",Datos_Personales)

#Eliminar un campo del diccionario
del Datos_personales["Ciudad"]
print("Diccionario eliminado":, Del)








#Como imprimo un diccionario?
print(Datos_Personales)    






