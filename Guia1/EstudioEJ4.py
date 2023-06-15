Persona1= input("Ingrese el nombre de la primera persona ")
Persona2= input("Ingrese el nombre de la segunda persona ")

if Persona1[0] and Persona2[0]:
    print ("La primera letra de la primera persona es ",[Persona1[0]])
    print ("La primera letra de la segunda persona es ", [Persona2[0]])
    print ("La Ultima letra de la primera persona es ",[Persona1[-1]])
    print ("La Ultima letra de la segunda persona es ", [Persona2[-1]]) 
    if [Persona1[0]]==[Persona2[0]]:
        print ("Las letras coinciden")
        
    if [Persona1[-1]]==[Persona2[-1]]:
        print ("Las ultimas letras coiciden") 
    if [Persona1[0]]!=[Persona2[0]]:
        print ("Las primeras letras no coiciden")
    if [Persona1[-1]]!=[Persona2[-1]]:
        print("Las ultimas letras no coiciden")               
    if [Persona1[-1][0]]!=[Persona2[-1][0]]:
        print("Por lo tanto las letras diferen, no son iguales")    





