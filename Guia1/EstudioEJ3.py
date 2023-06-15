Lado1 = (float(input("Ingresa el lado 1 del triangulo ")))
Lado2 = (float(input("ingresa el lado 2 del triangulo ")))
Lado3 = (float(input("Ingresa el lado 3 del triangulo ")))

if Lado1==Lado2 and Lado1==Lado3 and Lado2==Lado3:
    print ("El triangulo es un triangulo equilatero")
elif Lado1 == Lado2 or Lado2 == Lado3 or Lado1 == Lado3:
        print("El triángulo es isósceles.")

else:
      print("Es un triangulo escaleno")    

p= Lado1+Lado2+Lado3/2
area= p * (p-Lado1)*(p-Lado2)*(p-Lado3) **0.5
print("el area del triangulo es de",area) 
   