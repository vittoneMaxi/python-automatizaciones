print("primer archivo python")
nombre = input("¿Cómo te llamas? ")
print(f"¡Hola, {nombre}! Bienvenido al mundo de la automatización con Python.!ss!!!!!")



numeros = [5, -3, 0, 12, -9]

for numero in numeros:
    if numero > 0:
        print(numero, "es positivo")
    elif numero < 0:
        print(numero, "es negativo")
    else:
        print(numero, "es cero")