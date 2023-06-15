a = [21,8,15,3,12]
b = [10,9,12,15,18]
c = [2,3,8,9,12]

#a
lista_final= []
lista_final.extend(a)
lista_final.extend(b)
lista_final.extend(c)
print(lista_final)

#b
lista_final.insert(-1,20)
print(lista_final)

#c
lista_final.sort(reverse=True)
print(lista_final)

#d
lista_final.insert(16,4)
lista_final.insert(17,5)
lista_final.insert(18,6)

print(lista_final)

#e
lista_final.sort(reverse=True)
print(lista_final)
suma = sum(lista_final)
print (suma)
#f
promedio= sum(lista_final) / len(lista_final)
print(promedio)
#Letra D insertar la lista en la ultima posicion (d)
lista_final.append([4,5,6])
print(lista_final)





