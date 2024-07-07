"""
3.2.3 Guía de ejercicios resueltos (Clase 5)
EJERCICIO 2 Conjunto números primos
ACLARACIÓN: todavía no existe un mecanismo eficiente para obtener todos los
números primos, este ejemplo solo es aplicado a un nivel sencillo y básico, y sirve para
efectos de explicar el concepto de colecciones.
Desarrollen un programa que genere un conjunto de números primos dentro de un rango
específico. Utilicen un conjunto para almacenar los números primos y una función para
verificar si un número es primo.
"""
# Función para verificar si un número es primo
def es_primo(numero):
    if numero < 2:
        return False
    for i in range(2, numero):
        if numero % i == 0:
            return False
    return True

# Ingresar rango de números
while True:
    try:
        inicio = int(input("Ingrese el número de inicio: "))
        fin = int(input("Ingrese el número de fin: "))
    except ValueError:
        print("Debe ingresar un número entero.")
    else:
        if inicio < 0 or fin < 0:
            print("Los números deben ser positivos.")
        elif inicio > fin:
            print("El número de inicio debe ser menor que el número de fin.")
        else:
            break

# Crear una lista vacía para almacenar los números primos
primos = []
# Recorrer el rango de números
for i in range(inicio, fin+1):
    if es_primo(i):
        primos.append(i)
# Mostrar los números primos
print("Números primos en el rango de", inicio, "a", fin, "son:", primos)


