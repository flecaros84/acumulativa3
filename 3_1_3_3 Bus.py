"""
3.1.3 Actividad Matrices (Clase 2)
Ejercicio 3.
3. Crear un Arreglo [10][4] en el cual simula un bus, tendrá que darle de forma
automática los números de asiento y luego mostrarlo por pantalla
de la siguiente forma
1 2 3 4
5 6 7 8
9 10 11 12
13 14 15 16
17 18 19 20
21 22 23 24
25 26 27 28
29 30 31 32
33 34 35 36
37 38 39 40
"""
#Crear arreglo [10][4]
bus = [[0 for x in range(4)] for y in range(10)]
#Asignar valores al arreglo
for i in range(10):
    for j in range(4):
        bus[i][j] = i*4+j+1

#Mostrar arreglo
for i in range(10):
    for j in range(4):
        print(bus[i][j], end=" ")
    print()