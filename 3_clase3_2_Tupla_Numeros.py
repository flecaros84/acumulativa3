"""
Ejercicio 2: Operaciones con Tuplas Numéricas
Objetivo: Practicar el uso de funciones y métodos con tuplas.
1. Crea una tupla llamada `numeros` que contenga los números del 1 al 10.
2. Utiliza la función `sum()` para calcular la suma de los elementos de la tupla.
3. Utiliza las funciones `max()` y `min()` para encontrar el valor máximo y mínimo en la tupla.
4. Utiliza el método `count()` para contar cuántas veces aparece el número 5 en la tupla
"""
# Crear la tupla
numeros = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10)
# Calcular la suma de los elementos de la tupla
suma = sum(numeros)
# Encontrar el valor máximo y mínimo en la tupla
maximo = max(numeros)
minimo = min(numeros)
# Contar cuántas veces aparece el número 5 en la tupla
repeticiones = numeros.count(5)
# Imprimir los resultados
print(f"La suma de los elementos de la tupla es: {suma}")
print(f"El valor máximo en la tupla es: {maximo}")
print(f"El valor mínimo en la tupla es: {minimo}")
print(f"El número 5 aparece {repeticiones} veces en la tupla")
