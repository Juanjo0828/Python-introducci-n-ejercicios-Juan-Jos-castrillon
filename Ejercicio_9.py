"""
Título del Ejercicio:

Sistema de menú de restaurante

Descripción del Problema:

Desarrollar un programa que simule un menú de restaurante. El sistema debe mostrar opciones de platos, permitir al usuario elegir uno y calcular el total a pagar según el plato seleccionado.

Requisitos Específicos:

Mostrar un menú con al menos 3 platos y precios.

Pedir al usuario que elija una opción.

Validar que la opción exista.

Mostrar el nombre del plato elegido.

Mostrar el precio del plato.

Si la opción no es válida → mostrar error.

Los mensajes deben ser claros.

Ejemplo de entrada
1. Hamburguesa - $15
2. Pizza - $20
3. Ensalada - $10
Elige una opción: 2

Ejemplo de salida
Elegiste: Pizza
Total a pagar: $20
"""

print("Menú del restaurante")
print("1. Hamburguesa - $15")
print("2. Pizza - $20")
print("3. Ensalada - $10")

opcion = input("Elige una opción: ")

if opcion == "1":
    print("Elegiste: Hamburguesa")
    print("Total a pagar: $15")

elif opcion == "2":
    print("Elegiste: Pizza")
    print("Total a pagar: $20")

elif opcion == "3":
    print("Elegiste: Ensalada")
    print("Total a pagar: $10")

else:
    print("Opción no válida")
