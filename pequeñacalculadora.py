def suma(a, b):
    return a + b

def resta(a, b):
    return a - b

def multiplicacion(a, b):
    return a * b

def division(a, b):
    if b != 0:
        return a / b
    else:
        return "Error: No es posible dividir entre cero."

print("Selecciona una operación:")
print("1. Suma")
print("2. Resta")
print("3. Multiplicación")
print("4. División")

opcion = int(input("Ingresa el número de la operación deseada: "))

valor1 = float(input("Ingresa el primer valor: "))
valor2 = float(input("Ingresa el segundo valor: "))

if opcion == 1:
    resultado = suma(valor1, valor2)
    operacion = "+"
elif opcion == 2:
    resultado = resta(valor1, valor2)
    operacion = "-"
elif opcion == 3:
    resultado = multiplicacion(valor1, valor2)
    operacion = "*"
elif opcion == 4:
    resultado = division(valor1, valor2)
    operacion = "/"

print(f"El resultado de {valor1} {operacion} {valor2} es: {resultado}")
