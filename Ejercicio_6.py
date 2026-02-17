"""
Título del Ejercicio:

Simulador de semáforo

Descripción del Problema:

Desarrollar un programa que simule el funcionamiento de un semáforo. El sistema debe pedir el color del semáforo e indicar la acción que debe realizar el conductor.

Requisitos Específicos:

El programa debe pedir el color del semáforo usando input().

Debe convertir el texto a minúsculas.

Si el color es rojo → mostrar “detenerse”.

Si es amarillo → mostrar “precaución”.

Si es verde → mostrar “avanzar”.

Si el color no es válido → mostrar error.

Los mensajes deben ser claros.

Ejemplo de entrada:
Ingrese el color del semáforo: rojo

Ejemplo de salida:
Detenerse
"""

print("Simulador de semáforo")

color = input("Ingrese color del semáforo: ").lower()

if color == "rojo":
    print("Acción: detenerse")

elif color == "amarillo":
    print("Acción: precaución")

elif color == "verde":
    print("Acción: avanzar")

else:
    print("Error: color no válido")
