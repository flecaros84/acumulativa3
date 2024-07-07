"""
3.3.2 Guía de ejercicios (Clase 7)
EJERCICIO 2 ganadores de sorteo
Construir programa que permita almacenar los run ganadores del sorteo “la suerte de un
run”. Los run ganadores son todos los run que terminan en los últimos dígitos antes del
digito verificado sean 92, 95 y 84
Los datos deben ser leídos desde el archivo csv llamado “listadoRun.csv” y depositados
en el archivo llamado “ganadores.json”
run,nombre
10744679-6,Jose Haro
19881120-3,Daniela Almonacid
16112356-0,Carlos González
17651562-7,Andrea Soto
13429495-7,Luis Torres
17470063-K,Maria Rodríguez
19089980-2,Pablo Fernández
17449807-5,Valentina Pérez
13154134-1,Nicolás Vargas
14073175-7,Antonella Muñoz
24052019-2,Felipe Silva
27779771-2,Sofía López
23135155-8,Juan Díaz
25449950-1,Isabel Castro
22398351-0,Diego Morales
20449542-4,Ana Smith
27730053-2,Matías Araya
27358198-7,Valeria Mendoza
25130662-1,Gabriel Pérez
24981167-K,Martina Ruiz
22096175-3,Sebastián Herrera
23010574-K,Francisca Flores
24218263-4,Ricardo González
28942147-5,Constanza Álvarez
27165749-8,Javiera Troncoso
22216307-2,Eduardo Navarro
22425010-K,Catalina Vargas
23811768-2,Ángela Soto
24661213-7,Cristian Mora
20781422-9,Carla Contreras
10363927-1,Mauricio Rojas
12598545-9,Marcela Fernández
19105327-3,Felipe Montes
19539754-6,Alejandra Oyarzún
15731749-0,Pedro Ramírez
12865638-3,Daniela Aravena
10294021-0,Francisco Valdés
14104975-5,Florencia Rojas
11975810-6,Rodrigo Gómez
17500269-3,Amanda Guzmán
"""
import csv
import json

# Función para leer el archivo csv
def leer_csv(nombre_archivo):
    with open(nombre_archivo, "r", encoding="utf-8") as archivo:
        return list(csv.DictReader(archivo))

# Función para escribir el archivo json
def escribir_json(nombre_archivo, datos):
    with open(nombre_archivo, "w", encoding="utf-8") as archivo:
        json.dump(datos, archivo, indent=4, ensure_ascii=False)

# Función para extraer los datos del archivo csv
def extraer_csv(datos):
    ganadores = []
    for persona in datos:
        run = persona["run"]
        nombre = persona["nombre"]
        if run[6:8] == "92" or run[6:8] == "95" or run[6:8] == "84":
            ganadores.append({"run": run, "nombre": nombre})
    print(ganadores)
    escribir_json("ganadores.json", ganadores)

# Main
datos = leer_csv("listadoRun.csv")
extraer_csv(datos)