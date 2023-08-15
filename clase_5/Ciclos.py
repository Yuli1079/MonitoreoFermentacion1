#While 

VarControl = 1

while VarControl <=10: 
    
    print(VarControl)
    VarControl +=1 

#Arreglo o vector 
Listado = ['juan','pedro','maria','sofia']

#Posicion de inicio
b=0 

# Len permite sacar la matriz y tener todo el vector
# El ciclo permite ir hasta la ultima posicion de "Listado" iniciando b en 
# cero y repitiendose hasta la ultima posicion del vector o arreglo.
 
while b < len(Listado):
    print(Listado[b])
    b +=1

#Ciclo for 

frutas = ['limon', 'fresa', 'manzana', 'uva', 'naranja']

# la variable 'i' contiene ya el vector de frutas,  por lo tanto al imprimir i ya se contiene el arreglo.
for i in frutas:
    print(i)

# imprime numeros del 1 al 10.
for a in range(10): 
    print (a)

# Imprime en rango. 

for a in range(2,10): 
    print (a)

# Imprime segun se pide donde inicie, cantidad de aumento y valor hasta donde debe realizar el aumento.

for a in range(2,20,102): 
    print (a)

