"""
3.4.2 Guía de Ejercicios (Clase 11)
EJERCICIO 1 Calculadora con funciones
Creen un programa que emule la función de una calculadora, debe tener 4 funciones,
sumar, restar, dividir y multiplicar, el programa de permitir el ingreso de dos números de
tipo enteros. Este programa debe contener una pequeña validación que indique un
mensaje cuando se divide por 0, indicado que no se puede realizar la operación. Las
funciones a construir deben ser con argumentos y con retorno.

EJERCICIO 2 Incorporación de sentencias de validación
Al ejercicio anterior, le debemos incorporar una función de validación, que permita validar
que solo se puede ingresar números. Además, el ejercicio anterior no permite ingresar
valores decimales, a lo cual, en la misma función de validación se debe incorporar una
conversión de valor de tipo Int a valor de tipo Float
"""

def suma(numero1: int,numero2: int):
    return numero1+numero2

def resta(numero1,numero2):
    return numero1-numero2

def multiplicacion(numero1,numero2):
    return numero1*numero2

def division(numero1,numero2):
    try:
        numero1/numero2
    except ZeroDivisionError:
        print("No se puede dividir por 0.")
    else:
        print("La división de los números es:",numero1/numero2)

def validacion_numero(numero1,numero2):
    while True:
        try:
            numero1 = float(input("Ingrese el primer número: "))
            numero2 = float(input("Ingrese el segundo número: "))
        except ValueError:
            print("Debe ingresar un número real.")
        else:
            return numero1,numero2

#Programa principal
numero1 = 0
numero2 = 0
numero1,numero2 = validacion_numero(numero1,numero2)
while True:
    print("Elije una opción:")
    print("1. Sumar")
    print("2. Restar")
    print("3. Multiplicar")
    print("4. Dividir")
    print("5. Salir")
    try:
        opcion = int(input("Ingrese la opción: "))
    except ValueError:
        print("Debe ingresar un número entero.")
    if opcion == 1:
        print("La suma de los números es:",suma(numero1,numero2))
    elif opcion == 2:
        print("La resta de los números es:",resta(numero1,numero2))
    elif opcion == 3:
        print("La multiplicación de los números es:",multiplicacion(numero1,numero2))
    elif opcion == 4:
        division(numero1,numero2)
    elif opcion == 5:
        break
    else:
        print("Opción inválida.")