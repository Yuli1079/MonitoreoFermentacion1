# Ejercicio 1, Validacion de contraseña. 
contraseña = "Electronica05P"

clave = input("ingrese la contraseña: ")

if clave == contraseña: 
    print("La contraseña es correcta")

else: 

    print("Contraseña incorrecta")

# Ejercicio 2

Num1 = float(input("ingrese el dividendo: "))

while True: 
 
 Num2 = float(input( "ingrese el divisor  : "))

 if Num2 == 0 :

        print("El Valor del divisor no puede ser 0, ingrese otro valor:")   
 else :
     
    division = Num1 / Num2 
    print("El valor de la division es: ", division)
    break
 
# Ejercicio 3 

Numero = int(input("Ingrese un numero: "))

modulo = Numero % 2  

if modulo == 0 : 

    print ("El numero es par")

else :
    print ("El numero es impar")

# ejercicio 4 
    Edades=[12,34,18,16, 21]

for edad in Edades:
    if edad < 19:
        print("¡No puede ingresar!")
    else:
        print("¡BIENVENIDO!")
               


