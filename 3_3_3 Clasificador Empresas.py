"""
FICHA 3.3.3:
Actividad Formativa Archivos
En esta actividad, los estudiantes trabajarán individualmente para desarrollar un programa
que involucra el uso de archivos.
Construir programa que permita identificar las empresas que han tenido ventas inferiores a
$100.000.000, entre $100.000.001 y $200.000.000 y más de $200.000.000, a lo cual usted
deberá crear un archivo llamado “segmentacionEmpresas.json” que permita hacer esta dis-
tinción, a los datos listados más abajo deberá incorporar una columna adicional llamada
clasificacionEmpresa donde se indique “Pequeño Contribuyente”, “Mediano Contribuyente”
y “Gran Contribuyente”.
Datos de archivo de archivo “listadoRutEmpresa.csv”
rut,nombre,ventas
72642413-6,Comercial Calcetas Runner,150000000
76437473-2,Reparación Mac,300000000
76254356-9,ProgramaSoftware,27500000
76077262-3,Calzados Roma,15000000
76310800-8,Empresa Arcos,80000000
76283690-4,Casino Coffe,120000000
76952985-5,Cafe Express ltda,50000000
76081440-2,Vino Export SA,20000000
76216579-1,Cepa Merl LTDA,30000000
76597875-0,Comercial Ropa America,60000000
76852106-3,Empresas JP,90000000
76887745-8,Empresas ICata SA,100000000
76210124-2,Buses Peñalolen,150000000
76802052-4,Sandias Paine LTDA,70000000
76575973-1,Modas Junior P,400000000
76869384-2,Bar del 81,25000000
76877803-6,Empresas LLS,8000000
76706124-0,Empresas luz y vida SA,3000000
76162938-1,Empresa Matrix,120000000
"""
import csv
import json

#Función para leer archivo csv
def leer_archivo(archivo):
    with open(archivo, 'r',encoding='utf-8') as file:
        return file.readlines()

#Función para escribir archivo json
def escribir_archivo(archivo, data):
    with open(archivo, 'w',encoding='utf-8') as file:
        json.dump(data, file, indent=4, ensure_ascii=False)

#Función para clasificar empresas de acuerdo a sus ventas
def clasificar_empresa(ventas):
    if ventas < 100000000:
        return 'Pequeño Contribuyente'
    elif ventas >= 100000001 and ventas <= 200000000:
        return 'Mediano Contribuyente'
    else:
        return 'Gran Contribuyente'

#Función principal
def main():
    data = leer_archivo('listadoRutEmpresa.csv')
    #Lista de empresas
    empresas = []
    for empresa in data:
        #Extrae datos de la empresa desde una fila separada por comas
        rut, nombre, ventas = empresa.strip().split(',')
        #Convierte ventas a entero para facilitar clasificación
        ventas = int(ventas)
        clasificacion = clasificar_empresa(ventas)
        #Agrega empresas a lista de diccionarios
        empresas.append({
            'rut': rut,
            'nombre': nombre,
            'ventas': ventas,
            'clasificacion': clasificacion
        })
    escribir_archivo('segmentacionEmpresas.json', empresas)

if __name__ == '__main__':
    main()
