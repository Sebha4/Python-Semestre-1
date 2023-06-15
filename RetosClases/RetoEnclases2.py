print ("######## 07 DICCIONARIO ######")

Nombre=input ("Ingrese el nombre el alumno")
Asignatura=input("Ingrese el nombre de la asignatura")
Nota1= float(input("Ingrese la nota 1"))
Nota2= float(input("Ingrese la nota 2"))

Promedio= Nota1*0.30+Nota2*0.70
print("Su promedio es de", Promedio)


Dic= {
    "Nombre_Estudiante": Nombre,
    "Nombre_Asignatura": Asignatura,
    "Nota_1": Nota1,
    "Nota_2": Nota2,
    "Promedio": Promedio,
}

print(Dic)

