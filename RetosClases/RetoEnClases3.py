Ciudades = ["Santiago","Temuco","Osorno","Punta Arenas"]
ica = [134,99,245,50]

minimo = ica.index(min(ica))
print(f"La ciudad con el indice más bajo es {Ciudades[minimo]} con el indice más bajo {ica[minimo]}")

maximo = ica.index(max(ica))
print (f"La ciudad con el indice más alto es {Ciudades[maximo]} con el indice más alto {ica[maximo]}")

for i in range(len(Ciudades)):
    if ica [i] >= 0 and ica[i] <= 50:
        print(Ciudades[i],"Tiene una calidad del aire Buena")
    elif ica [i] >= 51 and ica[i] <= 100:
        print(Ciudades[i],"Tiene una calidad del aire moderada")  
    elif ica [i] >= 101 and ica[i] <= 150:
        print(Ciudades[i],"Tiene una calidad del aire dañina para la salud de un grupo sensible")  
    elif ica [i] >= 151 and ica[i] <= 200:
        print(Ciudades[i],"Tiene una calidad del aire dañina para la salud")  
    elif ica [i] >= 51 and ica[i] <= 100:
        print(Ciudades[i],"Tiene una calidad del aire muy dalina para la salud")          

