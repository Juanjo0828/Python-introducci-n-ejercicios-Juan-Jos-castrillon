#-----------------------------------------
# Nombre del Archivo: ejercicio_02.py
# Autor: Juan José Castrillón
# Fecha: 2026-02-17
# Descripción: Clasificador de calificaciones escolares
#-----------------------------------------

"""
1.Título del Ejercicio:
Clasificador de calificaciones escolares
2.Descripción del Problema:
Desarrollar un programa que solicite la calificación de un estudiante (de 0 a 100) y determine su desempeño académico. El programa debe mostrar un mensaje indicando si el estudiante reprobó, aprobó, obtuvo buen rendimiento o desempeño excelente.

Requisitos Específicos:

1.El programa debe pedir al usuario una calificación usando input().
2.La calificación debe convertirse a número entero.
3.El programa debe validar que la calificación esté entre 0 y 100.
4.Si la calificación es menor a 60 → reprobado.
5.Si está entre 60 y 79 → aprobado.
6.Si está entre 80 y 94 → buen rendimiento.
7.Si es 95 o más → desempeño excelente.
8.El programa debe mostrar un mensaje claro según el resultado.

Ejemplo de Entrada:

Ingrese la calificación: 85


Ejemplo de Salida Esperada:

Buen rendimiento académico

"""

print("bienvenido al sistema de calificaciones")
Calificaciones = int(input("por favor ingrese su calificacón final:"))
if Calificaciones <0:
    print("por favor ingrese una calificación valida")
elif Calificaciones >= 0 and Calificaciones < 60:
    print("reprobado")
elif Calificaciones >= 60 and Calificaciones < 80:
    print("Buen Rendimiento academico")
elif Calificaciones >= 80 and Calificaciones < 95:
    print("Excelente desempeño academico")
else:
    print("no se ingresaron calificaciones validas")


