tarifa_diurna = 12000
tarifa_nocturna = 16000
incremento_domingo_diurno = 2000
incremento_domingo_nocturno = 3000

horas_diurnas = int(input("Ingrese la cantidad de horas diurnas: "))
horas_nocturnas = int(input("Ingrese la cantidad de horas nocturnas: "))

empleados = [
    {
        "nombre": "Empleado 1",
        "turnos": ["Nocturno", "Nocturno", "Nocturno", "Diurno", "Diurno"],
    },
    {
        "nombre": "Empleado 2",
        "turnos": ["Nocturno", "Nocturno", "Nocturno", "Diurno", "Diurno", "Diurno"],
    },
    {
        "nombre": "Empleado 3",
        "turnos": ["Diurno", "Diurno", "Diurno", "Nocturno", "Nocturno"],
    },
]

for empleado in empleados:
    pago_diario = 0
    for turno in empleado["turnos"]:
        if turno == "Diurno":
            pago_diario += tarifa_diurna * horas_diurnas
        elif turno == "Nocturno":
            pago_diario += tarifa_nocturna * horas_nocturnas

    if "Diurno" in empleado["turnos"] and "Nocturno" in empleado["turnos"]:
        pago_diario += incremento_domingo_diurno + incremento_domingo_nocturno
    elif "Diurno" in empleado["turnos"]:
        pago_diario += incremento_domingo_diurno
    elif "Nocturno" in empleado["turnos"]:
        pago_diario += incremento_domingo_nocturno

    pago_semanal = pago_diario * 7

    empleado["pago_diario"] = pago_diario
    empleado["pago_semanal"] = pago_semanal


for empleado in empleados:
    print(f"Nombre: {empleado['nombre']}")
    print(f"Pago diario: {empleado['pago_diario']} CLP")
    print(f"Pago semanal: {empleado['pago_semanal']} CLP")
    print("-" * 30)