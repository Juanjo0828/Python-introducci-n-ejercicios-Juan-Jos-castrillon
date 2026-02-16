
"""
Manejo de edades para licencias de conducción
Descripción del Problema:
Desarrollar un programa que solicite la edad de una persona y determine si puede obtener una licencia de conducción según su rango de edad. El programa debe clasificar al usuario en categorías de elegibilidad y mostrar un mensaje claro indicando su situación.

Requisitos Específicos:

1. El programa debe pedir al usuario su edad mediante input().
2. La edad debe convertirse a un valor numérico entero.
3. Si la edad es menos a 16 años, el usuario no puede obtener licencia.
4. Si la edad está entre 16 y 17 años, puede obtener un permiso especial.
5. Si la edad es 18 años o más, puede obtener licencia completa.
6. El programa debe mostrar un mensaje explicativo según el caso.

7.El programa debe validar que la edad no sea negativa.
Ejemplo de Entrada (si aplica):
Ingrese su edad: 17
Salida esperada:
Puede obtener un permiso especial para conducir.

"""
print("Bienvenido al sistema de manejo de edades para licencias de conducción")

edad = int(input("Por favor, ingresa tu edad: "))
if  edad < 0: 
    print("Por favor, ingresa una edad valida, el sistema no admite edades negativas")
elif edad >= 16 and edad < 17:
    print("puedes obtener un permiso especial")
elif edad >= 18:
    print("puedes obtener una licencia B1 en adelante")
else: 
    print("No puedes obtener una licencia haata cumplir la mayoria de edad")
   
