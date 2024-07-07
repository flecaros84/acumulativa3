"""
Ejercicio 3: Rebanado de Tuplas
Objetivo: Practicar el rebanado (slicing) para obtener sub-tuplas.
1. Crea una tupla llamada `letras` que contenga las letras del alfabeto de la 'a' a la 'j'.
2. Utiliza el rebanado (slicing) para obtener una sub-tupla con las primeras 5 letras e
imprímela.
3. Utiliza el rebanado para obtener una sub-tupla con las últimas 3 letras e imprímela.
4. Utiliza el rebanado con pasos (saltos) para obtener una sub-tupla con cada segunda letra
e imprímela.
"""
# 1. Crea una tupla llamada `letras` que contenga las letras del alfabeto de la 'a' a la 'j'.
letras = ('a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j')
#Utiliza el rebanado (slicing) para obtener una sub-tupla con las primeras 5 letras e imprímela.
print(letras[:5])
#Utiliza el rebanado para obtener una sub-tupla con las últimas 3 letras e imprímela.
print(letras[-3:])
#Utiliza el rebanado con pasos (saltos) para obtener una sub-tupla con cada segunda letra e imprímela.
print(letras[::2])
