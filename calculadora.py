print ("Este programa realiza la operacion que desee; digite un numero teniendo en cuenta que + es suma, - es reta, * multiplicacion y / division")

operacion = (input("Ingrese el simbolo de la operacion que desea realizar: "))

print ("Ahora digite los numeros que desea operar: ")

num1= float(input("Ingrese el primer numero: "))
num2= float(input("Ingrese el segundo numero: "))

if operacion == "+" :
    suma= num1+num2
    print("El resultado es: ",suma)
elif operacion == "-": 
    resta= num1-num2 
    print("El resultado es: ",resta)
elif operacion == "*": 
    multiplicacion= num1*num2
    print("El resultado es: ",multiplicacion)

elif operacion == "/": 
    try: 
        division= num1/num2
    except ZeroDivisionError:

        if num2== 0:
             print("ERROR")
        else: 
            print("El resultado es: ",division)


