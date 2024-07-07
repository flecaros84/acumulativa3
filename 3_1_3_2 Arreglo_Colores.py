"""
2. Crear un Arreglo [3][3][3] manualmente, los valores del arreglo pueden ser
“amarillo”, “rojo”, “Naranja”, “Verde” y “Blanco”.
Una vez completado, mostrar la siguiente información:
● Número de elementos “amarillo”.
● Número de elementos “rojo”.
● Número de elementos “Naranja”.
● Número de elementos “Verde”.
● Número de elementos “Blanco”
"""
colores= [
    [#0
        [   "amarillo", "rojo",     "naranja"],     #0
        [   "verde",    "blanco",   "amarillo"],    #1
        [   "rojo",     "naranja",  "verde"]        #2
            #0          1           2
    ],
    [#1
        [   "blanco",   "amarillo", "rojo"],        #0
        [   "naranja",  "verde",    "blanco"],      #1
        [   "amarillo", "rojo",     "naranja"]      #2
            #0          1           2        
    ],
    [#2
        [   "verde",    "blanco",   "amarillo"],    #0
        [   "rojo",     "naranja",  "verde"],       #1
        [   "blanco",   "amarillo", "rojo"]         #2
            #0          1           2        
    ]
]
contador_amarillo = 0
contador_rojo = 0
contador_naranja = 0
contador_verde = 0
contador_blanco = 0

for capa in range (3):
    for fila in range (3):
        for columna in range (3):
            match colores[capa][fila][columna]:
                case "amarillo": 
                    contador_amarillo += 1
                case "rojo":
                    contador_rojo +=1
                case "naranja":
                    contador_naranja +=1
                case "verde":
                    contador_verde +=1
                case "blanco":
                    contador_blanco +=1

print(f"Los amarillos son: {contador_amarillo}")
print(f"Los rojos son: {contador_rojo}")
print(f"Los naranja son: {contador_naranja}")
print(f"Los verde son: {contador_verde}")
print(f"Los blancos son: {contador_blanco}")
            
