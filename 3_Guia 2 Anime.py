import json
import random

def cargar_biblioteca(archivo):
    try:
        with open(archivo, 'r') as leer:
            return json.load(leer)
    except FileNotFoundError:
        return []

def guardar_biblioteca(archivo, biblioteca):
    with open(archivo, "w") as f:
        json.dump(biblioteca, f, indent=4)

def registrar_anime(biblioteca, nombre, genero, numero_episodios, clasificacion):
    anime = {
        "nombre": nombre,
        "genero": genero,
        "numero_episodios": numero_episodios,
        "clasificacion": clasificacion
    }     
    biblioteca.append(anime)

def mostrar_biblioteca(biblioteca):
    for anime in biblioteca:
        print(f"Nombre: {anime['nombre']}, Genero: {anime['genero']}, N° Episodios: {anime['numero_episodios']}, clasificacion {anime['clasificacion']}\n")

def mostrar_genero(biblioteca, genero):
    for anime in biblioteca:
        if anime["genero"] == genero:
            print(f"Nombre: {anime['nombre']}, Genero: {anime['genero']}, N° Episodios: {anime['numero_episodios']}, clasificacion {anime['clasificacion']}\n")

#Obtener serie random de determinado genero
def recomendar_serie(biblioteca, genero):
    biblioteca_genero = []
    for anime in biblioteca:
        if anime["genero"] == genero:
            biblioteca_genero.append(anime)
    if len(biblioteca_genero) == 0:
        print("No se encontraron animes con ese genero")
    else:
        print(random.choice(biblioteca_genero))

archivo= "biblioteca.json"
biblioteca = cargar_biblioteca(archivo)
while True:
    print("Menu")
    print("1. Registrar Anime")
    print("2. Listar todos los animes")
    print("3. Buscar anime por genero")
    print("4. Recomendar anime")
    print("5. Salir")
    opcion = input("Ingrese su opción: ")
    if opcion=="1":
        nombre = input("Nombre: ")
        genero = input("Genero: ")
        numero_episodios = input("N° Episodios: ")
        clasificacion = input("clasificacion: ")
        registrar_anime(biblioteca, nombre, genero, numero_episodios,clasificacion)
        guardar_biblioteca(archivo, biblioteca)
    elif opcion == "2":
        mostrar_biblioteca(biblioteca)
    elif opcion == "3":
        genero = input("Ingrese el genero: ")
        mostrar_genero(biblioteca,genero)
    elif opcion == "4":
        genero = input("Ingrese el genero: ")
        recomendar_serie(biblioteca,genero)
    elif opcion == "5":
        break
    else:
        print("Ingrese una opción valida")
