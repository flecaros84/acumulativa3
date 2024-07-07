"""
3.1.2 Actividad listas (Clase 1)
Ejercicio 5
Cree un sistema de ventas de supermercado en el cual se pueda agregar productos
al carro de compras, las opciones del menú serán.
1. Agregar productos
2. Ver canasta
3. Ver total
4. Salir
 En agregar productos deberá mostrar un menú con 5 productos y sus
precios (creado por usted), cada vez que se seleccione un producto
quedará agregado en la lista.
 Ver canasta, es mostrar todos los productos seleccionados.
 Ver total, es mostrar el total a pagar por el cliente.
"""
# Se crea un diccionario con los productos y sus precios
productos = {
    "Leche": 1500,
    "Pan": 1000,
    "Huevos": 5000,
    "Carne": 10000,
    "Queso": 6000
}
# Se crea una lista vacía para almacenar los productos seleccionados
carro = []
# Se crea una variable para almacenar el total a pagar
total = 0
# Se crea menu

while True:
    print("1. Agregar productos")
    print("2. Ver canasta")
    print("3. Ver total")
    print("4. Salir")
    opcion = input("Seleccione una opción: ")
    if opcion == "1":
        print("Productos disponibles:")
        print("Producto - Precio")
        for producto in productos:
            print(f"{producto} ${productos[producto]}")
        producto = input("Seleccione un producto: ")
        if producto in productos:
            carro.append(producto)
            total += productos[producto]
        else:
            print("Producto no disponible")
    elif opcion == "2":
        print("Productos seleccionados:")
        for producto in carro:
            print(producto)
    elif opcion == "3":
        print(f"Total a pagar: ${total}")
    elif opcion == "4":
        break
    else:
        print("Opción no válida")

