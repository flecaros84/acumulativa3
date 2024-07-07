"""
3.3.2 Guía de ejercicios (Clase 7)
EJERCICIO 1 Validación de usuarios
Creen un programa que la lectura de un archivo CSV llamado 'datos.csv' que contiene
información sobre personas, incluyendo su nombre, edad y comuna. Para cada registro
en el archivo, se evalúa la edad y se determina si la persona es mayor o menor de edad.
La información, que incluye el nombre, la edad, el estado de edad y la comuna, se
imprime en la consola. Además, los registros de personas mayores o iguales a 25 años se
recopilan en una lista llamada mayores. La lista con usuarios mayores o iguales a 25 años
se guarda en un archivo JSON llamado 'mayores.json', se adjunta el conjunto de datos a
incorporar en datos.csv
"""
import csv
import json

def leer_csv(nombre_archivo):
    with open(nombre_archivo,'r',encoding='utf-8') as archivo:
        return list(csv.DictReader(archivo))

def escribir_json(nombre_archivo, datos):
    with open(nombre_archivo,'w',encoding='utf-8') as archivo:
        json.dump(datos, archivo, indent=4, ensure_ascii=False)

def extraer_csv(datos):
    poblacion = []
    mayores = []
    for persona in datos:
        nombre=persona['Nombre']
        edad=int(persona['Edad'])
        comuna=persona['Comuna']
        if edad>=25:
            estado = 'Mayor de edad'
            poblacion.append({'Nombre':nombre,'Edad':edad,'Comuna':comuna,'Estado':estado})
            mayores.append({'Nombre':nombre,'Edad':edad,'Comuna':comuna,'Estado':estado})
        else:
            estado = 'Menor de edad'
            poblacion.append({'Nombre':nombre,'Edad':edad,'Comuna':comuna,'Estado':estado})
    for persona in poblacion:
        print(persona)
    escribir_json('mayores.json', mayores)

datos = leer_csv('datos.csv')
extraer_csv(datos)
