"""
3.1.3.1 Crear un Arreglo [3][4] para luego ingresar elementos numéricos por pantalla
utilizando doble for, mostrar los elementos por pantalla de forma ordenada como
una matriz, tal cual muestra el ejemplo:
3 10 4 16
1 7 8 -7
9 -1 3 9
"""

arreglo = [
    #0 1 2 3
    [0,0,0,0],  #0
    [0,0,0,0],  #1
    [0,0,0,0]   #2
]

for fila in range (3):
    for columna in range (4):
        while True:    
            try: 
                arreglo[fila][columna] = int(input(f"Ingrese número de fila {fila} columna {columna}: "))
                break
            except ValueError:
                print("Debe ingresar un número.")
for fila in range (3):
    print(*arreglo[fila])