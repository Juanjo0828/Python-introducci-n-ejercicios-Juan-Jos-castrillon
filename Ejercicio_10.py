"""
Título del Ejercicio:

Conversor de monedas

Descripción del Problema:

Desarrollar un programa que permita convertir una cantidad de dinero entre pesos, dólares y euros. El sistema debe pedir la moneda de origen, la moneda de destino y el valor a convertir.

Requisitos Específicos:

Pedir la cantidad de dinero.

Pedir la moneda de origen (pesos/dólares/euros).

Pedir la moneda de destino.

Convertir el texto a minúsculas.

Validar que la moneda sea válida.

Mostrar el resultado de la conversión.

Mostrar error si los datos no son válidos.

(Usaremos tasas de ejemplo)
1 dólar = 4000 pesos
1 euro = 4500 pesos

Ejemplo de entrada:
Cantidad: 10
Moneda origen: dolares
Moneda destino: pesos

Ejemplo de salida:
Resultado: 40000 pesos
"""

print("Conversor de monedas")

cantidad = float(input("Ingrese la cantidad: "))
origen = input("Moneda origen (pesos/dolares/euros): ").lower()
destino = input("Moneda destino: ").lower()

if origen == "pesos":
    en_pesos = cantidad
elif origen == "dolares":
    en_pesos = cantidad * 4000
elif origen == "euros":
    en_pesos = cantidad * 4500
else:
    print("Moneda de origen no válida")
    exit()

if destino == "pesos":
    resultado = en_pesos
elif destino == "dolares":
    resultado = en_pesos / 4000
elif destino == "euros":
    resultado = en_pesos / 4500
else:
    print("Moneda de destino no válida")
    exit()

print("Resultado:", resultado, destino)
