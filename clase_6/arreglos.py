Var = 1
#Se crea un arreglo. 

VarLista = ['hola', '1', '2', '3.5'] 
varlista = ['Hector', True, 5.5, 8]
print(varlista[3])

#Elimina un elemento de la lista
del varlista[0]

#Agrega un elemento a la lista 
varlista.insert(1,"cual")

#Agrega unn elemento siempre al final
varlista.append('USCO')

#Agrega una variable que la persona quiera agregar
varlista.append(input("Insete la variable para agrear a la lista"))



#Imprimir una lista con ciclo for 

""" """ """
for z in varlista:
    print(z)

#Imprimir lista con ciclo while 

q = 0

while q < (len(varlista)):

    print(varlista[q])
    q +=1

""" """ """