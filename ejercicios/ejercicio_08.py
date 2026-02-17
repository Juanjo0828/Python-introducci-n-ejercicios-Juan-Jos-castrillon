#-----------------------------------------
# Nombre del Archivo: ejercicio_08.py
# Autor: Juan José Castrillón
# Fecha: 2026-02-17
# Descripción: Clasificación de temperatura
#-----------------------------------------

"""
Descripción del Problema:

Desarrollar un programa que solicite la temperatura actual y la clasifique como fría, templada o caliente según su valor.

Requisitos Específicos:

El programa debe pedir la temperatura usando input().

Debe convertirla a número decimal (float).

Validar que la temperatura no sea un valor inválido.

Si la temperatura es menor a 10 → frío.

Si está entre 10 y 25 → templado.

Si es mayor a 25 → calor.

Mostrar un mensaje claro al usuario.

Ejemplo de entrada:
Ingrese la temperatura: 18

Ejemplo de salida
Clima templado
"""

print("Clasificador de temperatura")

temperatura = float(input("Ingrese la temperatura: "))

if temperatura < -100 or temperatura > 100:
    print("Error: temperatura inválida")

elif temperatura < 10:
    print("Clima frío")

elif temperatura <= 25:
    print("Clima templado")

else:
    print("Clima caluroso")