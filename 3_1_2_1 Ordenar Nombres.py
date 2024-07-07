"""
3.1.2.1 Escriba un programa que permita almacenar 3 nombres solicitados por pantalla en
una lista, luego el sistema deberá mostrar el nombre que tenga mayor cantidad de
caracteres en un mensaje de salida por pantalla.
"""
lista_nombres = []
for i in range(3):
    nombre_ingresado = input("Ingrese un nombre: ")
    lista_nombres.append(nombre_ingresado)
# Ordena la lista de nombres por la cantidad de caracteres, de menor a mayor
lista_nombres.sort(key=len)
print(f"El nombre con mayor cantidad de caracteres es: {lista_nombres[-1]}")