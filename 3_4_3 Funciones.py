"""
Actividad Funciones (Clase 11)
Objetivo del programa: Un programa funcional que, dada una lista de números
ingresada por el usuario, identifica y muestra los números pares e impares de
manera clara y organizada.
Reglas de negocio:
1. Solicitar al usuario que ingrese una lista de números enteros
separados por espacios.
2. Implementar una función llamada validar_lista_numeros que verifique
que todos los elementos ingresados sean números enteros. Si se
ingresa algún valor no válido, solicitar nuevamente la lista.
3. la función validar_lista_numeros debe utilizar un bucle y maneja
excepciones para asegurar que todos los elementos ingresados sean
números enteros.
4. Utilizar el operador de módulo % (MOD) para determinar si un
número es par o impar en la lista de números a ingresar. Considerar
que un número es par cuando el mod es igual a 0, en caso contrario,
es impar
5. Crear dos listas separadas: una para los números pares y otra para
los impares.
6. Mostrar al usuario las listas resultantes, indicando los números
pares, e indicando los números impares
"""
#Ingresar lista de números
def validar_lista_numeros():
    while True:
        try:
            lista_numeros = input("Ingrese una lista de números enteros separados por espacios: ").split()
            lista_numeros = [int(numero) for numero in lista_numeros]
        except ValueError:
            print("Debe ingresar números enteros.")
        else:
            return lista_numeros

def par_impar(lista_numeros):
    #Crear listas vacías para almacenar los números pares e impares
    pares = []
    impares = []
    #Recorrer la lista de números
    for numero in lista_numeros:
        #Determinar si el número es par o impar
        if numero % 2 == 0:
            pares.append(numero)
        else:
            impares.append(numero)
    return pares,impares

#Programa principal
lista_numeros = validar_lista_numeros()
pares,impares = par_impar(lista_numeros)
print("Los números pares son:",pares)
print("Los números impares son:",impares)
