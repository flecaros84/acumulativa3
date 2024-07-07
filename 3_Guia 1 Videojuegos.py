"""
Guía 1: Sistema de Gestión de Torneos de Videojuegos
Objetivos de Aprendizaje
- Comprender y aplicar conceptos de estructuras de datos en Python.
- Implementar funciones para registrar, listar y manejar datos temporales.
- Utilizar archivos para la persistencia de datos.
- Integrar el uso de GitHub para el manejo de versiones y colaboración.
Descripción del Ejercicio
En este ejercicio, desarrollarás una aplicación en Python que permita registrar y gestionar
inscripciones a torneos de videojuegos. Los torneos disponibles son para los juegos más
populares del año: "Fortnite", “League of Legends" y "Valorant".
La aplicación debe proporcionar las siguientes funcionalidades:
1. Registrar Inscripción: Recoge la información del jugador, incluyendo su nombre, apellido,
ciudad de origen y el videojuego en el que desea inscribirse.
2. Listar Todas las Inscripciones: Muestra una lista con todas las inscripciones realizadas.
3. Imprimir Detalle de Inscripciones por Videojuego: Permite seleccionar un videojuego y
genera un archivo de texto con el detalle de todas las inscripciones para ese juego.
4. Salir del Programa: Termina la ejecución del programa.
Conceptos Clave
1. Funciones en Python: Las funciones permiten dividir el código en bloques manejables y
reutilizables. En este ejercicio, crearás funciones para manejar las inscripciones y generar
archivos.
2. Estructuras de Datos: Usarás listas para almacenar las inscripciones, aprovechando su
capacidad de contener colecciones de datos heterogéneos.
3. Manejo de Archivos: Aprenderás a crear y escribir en archivos de texto, una habilidad
fundamental para la persistencia de datos.
4. Control de Versiones con GitHub: Subirás tu código a GitHub, lo cual no solo facilita la
colaboración, sino que también permite llevar un control de versiones de tu proyecto.
¿Qué es un README.md?
Un archivo `README.md` es un documento esencial en cualquier repositorio de GitHub.
Proporciona una descripción del proyecto, instrucciones de uso, requisitos y cualquier otra
información relevante para los usuarios del proyecto. En este ejercicio, deberás crear un
archivo `README.md` que incluya:
- Descripción del Proyecto: Explica brevemente de qué se trata tu aplicación.
- Instrucciones de Uso: Describe cómo ejecutar el programa y cómo utilizar sus
funcionalidades.
- Requisitos: Lista las dependencias necesarias para ejecutar el programa (por ejemplo,
Python 3.x).
"""
import json

# Cargar archivo con registros
def Cargar_Archivo(archivo):
    try:
        with open(archivo, 'r') as leer:
            return json.load(leer)
    except FileNotFoundError:
        return []

# Guardar archivo    
def Guardar_Archivo(archivo, registro):
    with open(archivo, "w") as f:
        json.dump(registro, f, indent=4)

# Registrar jugador
def Registrar_Jugador(registro):
    nombre = input("Ingrese el nombre del jugador: ")
    apellido = input("Ingrese el apellido del jugador: ")
    ciudad = input("Ingrese la ciudad del jugador: ")
    juego = Seleccionar_Juego()
    jugador = { 
                "nombre": nombre,
                "apellido": apellido,
                "ciudad": ciudad,
                "juego": juego
    }
    registro.append(jugador)

# Mostrar todas las inscripciones
def Listar_Inscripciones(registro):
    for jugador in registro:
        print(f"Nombre: {jugador["nombre"]},Apellido: {jugador["apellido"]},Ciudad: {jugador["ciudad"]},Juego: {jugador["juego"]}\n")

# Seleccionar juego
def Seleccionar_Juego():
    while True:
        try:
            print("Selecciona un juego:")
            print("1. Fornite")
            print("2. League of Legends")
            print("3. Valorant")
            opcion = int(input("Ingrese n° de selección: "))
        except ValueError:
            print("Opción invalida")
        else:
            match opcion:
                case 1:
                    return "Fornite"
                case 2:
                    return "League of Legends"
                case 3:
                    return "Valorant"
                case _:
                    print("Opción invalida")

# Imprimir detalle inscripciones de un juego determinado en txt   
def Imprimir_Detalle(registro):
    juego = Seleccionar_Juego()
    try:
        with open(f"{juego}.txt", "w") as f:
            for jugador in registro:
                if jugador["juego"] == juego:
                    f.write(f'{jugador["nombre"]},{jugador["apellido"]},{jugador["ciudad"]}\n')
    except FileNotFoundError:
        print("No se pudo crear el archivo")

# Programa principal
def main():
    archivo = "registro.json"
    registro = Cargar_Archivo(archivo)
    while True:
        print("Menu")
        print("1. Registrar Inscripción")
        print("2. Listar las Inscripciones")
        print("3. Imprimir detalle de inscripciones de un juego")
        print("4. Salir")
        try:
            opcion = int(input("Ingrese una opción: "))
        except ValueError:
            print("Opción inválida")
        else:
            match opcion:
                case 1:
                    Registrar_Jugador(registro)
                    Guardar_Archivo(archivo, registro)
                case 2:
                    Listar_Inscripciones(registro)
                case 3:
                    Imprimir_Detalle(registro)
                case 4:
                    break
                case _:
                    print("Opción inválida")

if __name__ == "__main__":
    main()
