TemperaturasMínimas= {9, 5, 2, 7, 6, 1}
TemperaturasMáximas= {12, 14, 11, 10, 15, 9}

#A
if 9 in TemperaturasMáximas and TemperaturasMáximas:
    print("la temperatura 9C se encuentra en ambos sets")
else:
    print("la temperatura 9C no se encuentra en ambos sets")   

#B

if 6 in TemperaturasMínimas and TemperaturasMáximas:
    print ("el 6 se encuentra en una de las listas")
else:
    print("La temperatura 6 no se encuentra en una de las listas")
if  17 in TemperaturasMáximas and TemperaturasMínimas:
        print("el 17 se encuentra en una de las listas")  
else:
    print("el 17 no se encuentra en ninguna de las listas")  

#C
TemperaturasMínimas1= {x + 4 for x in TemperaturasMínimas}   
TemperaturasMáximas1= {x + 4 for x in TemperaturasMáximas}  
print("La temperatura de la lista TemperaturaMinima a sido eleveda a 4", TemperaturasMínimas1)
print("La temperatura de la lista TemperaturaMaxima a sido eleveda a 4", TemperaturasMáximas1)

#D

unionSets= TemperaturasMínimas.union(TemperaturasMáximas)
print("Esta es la union de ambos sets",unionSets)




        


    
    

