"""
Ejercicio 1: Información Personal
Objetivo: Practicar la creación y acceso a elementos de tuplas.
1. Crea una tupla llamada `informacion` que contenga los siguientes elementos en orden: tu
nombre, tu edad, y tu ciudad de residencia.
2. Accede e imprime cada elemento de la tupla utilizando índices.
3. Utiliza el desempaquetado de tuplas para asignar los valores a variables individuales y
luego imprime estas variables.
"""
# 1. Crear la tupla
informacion = ('Fabián', 39, 'Puerto Montt')
# 2. Acceder e imprimir cada elemento de la tupla
print(informacion[0])
print(informacion[1])
print(informacion[2])
# 3. Desempaquetar la tupla
nombre, edad, ciudad = informacion
print(nombre)
print(edad)
print(ciudad)