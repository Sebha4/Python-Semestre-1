#Laboratorio escrito

trabajadores = [
    ["Juan", [700000, 650000, 690000]],
    ["María", [681000, 710000, 590000]],
    ["Pedro", [590000, 635000, 705000]]
]

#1
def promedio_sueldos(sueldos):
    return round(sum(sueldos) / len(sueldos), 2)

#2
def impuesto_retenido(sueldo):
    return round(sueldo * 0.1225, 2)

