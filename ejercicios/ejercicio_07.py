#-----------------------------------------
# Nombre del Archivo: ejercicio_07.py
# Autor: Juan José Castrillón
# Fecha: 2026-02-17
# Descripción: Sistema básico de verificación de contraseña
#-----------------------------------------

"""
Título del Ejercicio:

Sistema básico de verificación de contraseña

Descripción del Problema:

Desarrollar un programa que solicite una contraseña al usuario y verifique si es correcta. El sistema debe permitir o negar el acceso según la contraseña ingresada.

Requisitos Específicos:

1.El programa debe pedir una contraseña usando input().
2.Debe comparar con una contraseña guardada en el sistema.
3.Si la contraseña es correcta → acceso permitido.
4.Si es incorrecta → acceso denegado.
5.El programa debe mostrar mensajes claros.
Debe validar que no esté vacía.

Ejemplo de entrada:
Ingrese contraseña: 1234

Ejemplo de salida:
Acceso permitido
"""

print("Sistema de verificación de contraseña")

contraseña_correcta = "1234"
contraseña = input("Ingrese contraseña: ")

if contraseña == "":
    print("Error: no puede estar vacía")

elif contraseña == contraseña_correcta:
    print("Acceso permitido")

else:
    print("Acceso denegado")


