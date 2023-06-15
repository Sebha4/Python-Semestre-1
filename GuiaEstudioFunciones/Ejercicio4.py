def desglosar_vuelto(vuelto):
    billetes = [10000, 5000, 2000, 1000, 500, 100, 50, 10, 5, 1]
    resultado = {}

    for billete in billetes:
        if vuelto >= billete:
            cantidad = vuelto // billete
            resultado[billete] = cantidad
            vuelto -= cantidad * billete

    return resultado


def cajero_supermercado():
    print("-------------------------[Cajero SuperMercado]-------------------------------------")
    opcion = input("¿Desea ingresar los valores uno por uno o el pago total? \n1: uno por uno \n2: pago total ")

    if opcion == "1":
        total = 0
        valor = 0

        while True:
            valor = float(input("Ingrese un valor (0 para finalizar): "))

            if valor == 0:
                break

            total += valor

        pago = float(input("Ingrese la cantidad pagada: "))

    elif opcion == "2":
        total = float(input("Ingrese el total de la compra: "))
        pago = float(input("Ingrese la cantidad pagada: "))

    else:
        print("Opción inválida.")
        return

    if pago < total:
        print("El pago no es suficiente.")
        return

    vuelto = pago - total
    desglose = desglosar_vuelto(int(vuelto))

    print("Vuelto total: $", vuelto)
    print("Desglose de vuelto:")
    for billete, cantidad in desglose.items():
        print("$", billete, ":", cantidad)


cajero_supermercado()