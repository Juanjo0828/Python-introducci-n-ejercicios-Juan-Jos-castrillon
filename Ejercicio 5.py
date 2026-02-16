"""
Título del Ejercicio:

Sistema básico de cajero automático

Descripción del Problema:

Desarrollar un programa que simule el retiro de dinero en un cajero automático. El sistema debe pedir el saldo disponible del usuario y el monto que desea retirar. El programa debe validar que el retiro no supere el saldo y mostrar el saldo restante.

Requisitos Específicos:

1. El programa debe pedir el saldo inicial del usuario.
2. Debe pedir el monto que desea retirar.
3. Ambos valores deben convertirse a float.
4. El programa debe validar que los valores no sean negativos.
5. Si el retiro supera el saldo → mostrar error.
6. Si el retiro es válido → descontar y mostrar saldo restante.

Los mensajes deben ser claros.

Ejemplo de entrada:
Ingrese su saldo inicial: 1000
Ingrese el monto a retirar: 300

Ejemplo de salida:
Saldo restante: 700.0
"""

print("Cajero automático")

saldo = float(input("Ingrese su saldo: "))
retiro = float(input("Ingrese monto a retirar: "))

if saldo < 0 or retiro < 0:
    print("Error: los valores no pueden ser negativos")

elif retiro > saldo:
    print("Fondos insuficientes")

else:
    saldo_restante = saldo - retiro
    print("Retiro exitoso")
    print("Saldo restante:", saldo_restante)