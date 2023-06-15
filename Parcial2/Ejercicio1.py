palabra= input("Ingrese una palabra: ")
palabraAL= ""

palabraAL= palabraAL.lower()
palabra= palabra.lower()

for i in range (len(palabra)-1,-1,-1):
    palabraAL += palabra[i]

if palabraAL == palabra:
    print("La palabra es un palindromo")
else:
    print("La palabra no es un palindromo")    
