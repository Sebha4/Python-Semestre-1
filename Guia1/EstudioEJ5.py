Nota1= float(input("Ingrese la primera nota "))
Nota2= float(input("Ingrese la segunda nota "))
Nota3= float(input("Ingrese la tercera nota "))

PromedioPonderado  = Nota1 * 0.3 + Nota2 * 0.4 + Nota3 * 0.3
print (PromedioPonderado)

if PromedioPonderado <4.0:
    print("El estudiante ha reprobado La asignatura")
if PromedioPonderado >= 4.0:
    print("El estudiante ha aprobado la asignatura")
if PromedioPonderado >=6.0:
    print("El estudiante aprobo con distincion la asignatura")
