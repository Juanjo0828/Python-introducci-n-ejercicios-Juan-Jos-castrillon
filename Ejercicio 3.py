"""
Título del Ejercicio:

Sistema básico de manejo de usuarios para una compraventa

Descripción del Problema:

Desarrollar un programa que simule el registro de usuarios en una compraventa. El sistema debe pedir el nombre del usuario y su tipo (cliente o empleado), y mostrar un mensaje diferente según el tipo de usuario registrado.

Requisitos Específicos:

1. El programa debe pedir el nombre del usuario.
2. Debe pedir el tipo de usuario: "cliente" o "empleado".
3. El programa debe convertir el tipo de usuario a minúsculas.
4. Si el usuario es cliente → mostrar mensaje de bienvenida como cliente.
5. Si es empleado → mostrar acceso a funciones administrativas.
6. Si el tipo ingresado no es válido → mostrar error.
7. El programa debe mostrar mensajes claros y ordenados.

Ejemplo de Entrada:
Ingrese su nombre: Juan
Ingrese tipo de usuario (cliente/empleado): cliente

Ejemplo de Salida:
Bienvenido Juan, registrado como cliente.
"""
print("Sistema de manejo de usuarios - Compraventa")
nombre = input("Ingrese su nombre: ")
tipo_usuario = input("Ingrese tipo de usuario (cliente/empleado): ")
if tipo_usuario == "cliente":
    print("Bienvenido", nombre + ", registrado como cliente.")
elif tipo_usuario == "empleado":
    print("Bienvenido", nombre + ", acceso a funciones administrativas concedido.")
else:
    print("Error: tipo de usuario no válido.")


        
    
        



