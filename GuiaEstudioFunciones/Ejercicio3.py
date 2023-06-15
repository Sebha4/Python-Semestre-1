año=int(input("ingrese un año:\n>"))

def bisiesto(año):

    if año % 4 != 0:
        return False
    elif año % 100 != 0:
        return True
    elif año % 400 != 0:
        return False
    else:
        return True

if bisiesto(año):
    print(año, "es un año bisiesto.")
else:
    print(año, "no es un año bisiesto.")
