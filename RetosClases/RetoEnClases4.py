nombre1= input("Ingresa el nombre del primer paciente: " )
nombre2= input("Ingresa el nombre del segundo paciente: " )
nombre3= input("Ingresa el nombre del Tercer paciente: " )
Nombres = {nombre1,nombre2,nombre3}

Peso1= input("Ingresa el Peso del primer paciente: " )
Peso2= input("Ingresa el Peso del Segundo paciente: " )
Peso3= input("Ingresa el Peso del Tercer paciente: " )
Peso = [Peso1,Peso2,Peso3]

Estatura1= input("Ingresa La estatura del primer paciente: " )
Estatura2= input("Ingresa La estatura del segundo paciente: " )
Estatura3= input("Ingresa La estatura del Tercer paciente: " )
Estaturas= {Estatura1,Estatura2,Estatura3}



Edad1= int(input("Ingresa La Edad del primer paciente: "))
 
while Edad1 <= 0 and Edad1 >= 130:
     print("Ingrese una edad valida",Edad1)

Edad2= int(input("Ingresa La Edad del Segundo paciente"))
while Edad2 <= 0 and Edad2 >= 130:
     print("Ingrese una edad valida",Edad2)
    

Edad3= int(input("Ingresa La Edad del Tercer paciente:"))
while Edad2 <= 0 and Edad3 >=130:
    print("Ingrese una edad valida",Edad3)
Edades = {Edad1,Edad2,Edad3}    

print ("Aqui esta la informacion de todo")
tuple=[Nombres,Peso,Estaturas,Edades]
print(":" ,tuple)    

