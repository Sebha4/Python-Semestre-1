#a
regiones = {
    "Nombre": "Los Ríos",
        "Superficie (Km2)": 18429,
        "Habitantes (2017)": 404432
        
    
}, {
        "Nombre": "Magallanes",
        "Superficie (Km2)": 1382291,
        "Habitantes (2017)": 166533
}

print("Este es el diccionario de regiones",regiones)
#b
for regiones in regiones.values():
    densidad = round(regiones["habitantes en 2017"]) / regiones["Superficie "], 1
    regiones["Densidad"] 

#c 
regiones[14]["Capital"] = "Valdivia"
regiones[12]["Capital"] = "Punta Arenas"    
