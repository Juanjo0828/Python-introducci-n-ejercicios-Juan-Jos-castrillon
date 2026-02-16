"""
Título del Ejercicio:

Sistema de descuentos en una tienda

Descripción del Problema:

Desarrollar un programa que solicite el monto de compra de un cliente y calcule el descuento aplicado según el valor de la compra. El sistema debe mostrar el descuento obtenido y el total a pagar.

Requisitos Específicos:

1. El programa debe pedir el monto de compra usando input().
2. El monto debe convertirse a número decimal (float).
3. El programa debe validar que el monto no sea negativo.
4. Si el monto es menor a 50 → no hay descuento.
5. Si el monto está entre 50 y 99 → descuento del 5%.
6. Si el monto está entre 100 y 199 → descuento del 10%.
7. Si el monto es 200 o más → descuento del 20%.
8. El programa debe mostrar:
9. porcentaje de descuento
10. valor descontado
11. total a pagar
12. Los mensajes deben ser claros y ordenados.

Ejemplo de entrada:
Ingrese el monto de compra: 120

Ejemplo de salida:
Descuento aplicado: 10.0 %
Valor descontado: 12.0
Total a pagar: 108.0
"""
print("Sistema de descuentos - Tienda")

monto = float(input("Ingrese el monto de compra: "))

if monto < 0:
    print("Error: el monto no puede ser negativo")

elif monto < 50:
    descuento = 0

elif monto < 100:
    descuento = 0.05

elif monto < 200:
    descuento = 0.10

else:
    descuento = 0.20

valor_descuento = monto * descuento
total = monto - valor_descuento

print("Descuento aplicado:", descuento * 100, "%")
print("Valor descontado:", valor_descuento)
print("Total a pagar:", total)