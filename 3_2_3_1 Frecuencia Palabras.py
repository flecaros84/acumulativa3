"""
3.2.3 Guía de ejercicios resueltos (Clase 5)
EJERCICIO 1 Frecuencia de palabras de un texto
Creen un programa que solicite a los usuarios ingresar un texto. Luego, el programa debe
analizar el texto y mostrar la frecuencia de cada palabra. Utilicen un diccionario para
almacenar las palabras como claves y la frecuencia como valores.
"""
#Solicitar al usuario que ingrese un texto
texto = input("Ingrese un texto: ")

#Separar el texto en palabras
palabras = texto.split()

#Crear un diccionario vacío
frecuencia = {}

#Recorrer la lista de palabras
for palabra in palabras:
    #Si la palabra no está en el diccionario
    if palabra not in frecuencia:
        #Agregar la palabra al diccionario con frecuencia 1
        frecuencia[palabra] = 1
    else:
        #Si la palabra ya está en el diccionario, incrementar la frecuencia
        frecuencia[palabra] += 1

#Mostrar la frecuencia de cada palabra
for palabra, cantidad in frecuencia.items():
    print(f"La palabra '{palabra}' aparece {cantidad} veces en el texto.")
