# Importa el modulo tkinter para la interfaz grafica
import tkinter as tk
# Importa el modulo requests para hacer peticiones a la API
import requests
# Importa BytesIO para los datos binarios
from io import BytesIO
# Para trabajar con las imagenes de los pokemon
from PIL import Image, ImageTk
# Importa el modulo random para obtener un pokemon aleatorio
import random

def buscar_pokemon():
    nombre_pokemon = entry_pokemon.get().lower()
    url = f"https://pokeapi.co/api/v2/pokemon/{nombre_pokemon}"
    # Solicitud get a la API mediante la URL
    response = requests.get(url)
    # Verifica si la solicitud fue exitosa
    if response.status_code == 200:
        pokemon = response.json()
        nombre = pokemon["name"].capitalize()
        id = pokemon["id"]
        tipos = [tipo["type"]["name"] for tipo in pokemon["types"]]
        # Capitalizar los tipos
        tipos = [tipo.capitalize() for tipo in tipos]
        resultado = f"Nombre: {nombre}\nID: {id}\nTipos: {'/'.join(tipos)}"
        # Obtener ataque, defensa, ataque especial, defensa especial y velocidad
        stats = pokemon["stats"]
        for stat in stats:
            nombre_stat = stat["stat"]["name"]
            base_stat = stat["base_stat"]
            resultado += f"\n{nombre_stat.capitalize()}: {base_stat}"
        # Obtener imagen del pokemon
        imagen_url = pokemon["sprites"]["front_default"]
        # Realiza una solicitud get a la URL de la imagen
        imagen_response = requests.get(imagen_url)
        # Abre la img con BytesIO
        imagen = Image.open(BytesIO(imagen_response.content))
        # Redimensiona la imagen
        imagen = imagen.resize((200, 200), Image.Resampling.LANCZOS)
        # Convierte la imagen a un objeto de tkinter
        foto = ImageTk.PhotoImage(imagen)
        label_imagen.config(image=foto)
        # Guarda la referencia de la imagen para que no sea eliminada por el recolector de basura
        label_imagen.image = foto
        # Obtener descripcion del pokemon
        descripcion_url = f"https://pokeapi.co/api/v2/pokemon-species/{id}"
        descripcion_response = requests.get(descripcion_url)
        descripcion = descripcion_response.json()
        # Obtiene el flavor text
        flavor_text = descripcion["flavor_text_entries"]
        # Obtiene la descripcion en español
        descripcion_esp = [descripcion["flavor_text"] for descripcion in flavor_text if descripcion["language"]["name"] == "es"]
        resultado += f"\nDescripción: {descripcion_esp[0]}"
    else:
        resultado = "Pokemon no encontrado"
        # Elimina la imagen del label si no se encuentra el pokemon
        label_imagen.config(image=None)
    # Configura la etiqueta label para mostrar la información del pokemon
    label_resultado.config(text=resultado)

def pokemon_aleatorio():
    numero_pokemon = random.randint(1, 1025)
    url = f"https://pokeapi.co/api/v2/pokemon/{numero_pokemon}"
    # Solicitud get a la API mediante la URL
    response = requests.get(url)
    # Verifica si la solicitud fue exitosa
    if response.status_code == 200:
        pokemon = response.json()
        nombre = pokemon["name"].capitalize()
        id = pokemon["id"]
        tipos = [tipo["type"]["name"] for tipo in pokemon["types"]]
        # Capitalizar los tipos
        tipos = [tipo.capitalize() for tipo in tipos]
        resultado = f"Nombre: {nombre}\nID: {id}\nTipos: {'/'.join(tipos)}"
        # Obtener ataque, defensa, ataque especial, defensa especial y velocidad
        stats = pokemon["stats"]
        for stat in stats:
            nombre_stat = stat["stat"]["name"]
            base_stat = stat["base_stat"]
            resultado += f"\n{nombre_stat.capitalize()}: {base_stat}"
        # Obtener imagen del pokemon
        imagen_url = pokemon["sprites"]["front_default"]
        # Realiza una solicitud get a la URL de la imagen
        imagen_response = requests.get(imagen_url)
        # Abre la img con BytesIO
        imagen = Image.open(BytesIO(imagen_response.content))
        # Redimensiona la imagen
        imagen = imagen.resize((200, 200), Image.Resampling.LANCZOS)
        # Convierte la imagen a un objeto de tkinter
        foto = ImageTk.PhotoImage(imagen)
        label_imagen.config(image=foto)
        # Guarda la referencia de la imagen para que no sea eliminada por el recolector de basura
        label_imagen.image = foto
        # Obtener descripcion del pokemon
        descripcion_url = f"https://pokeapi.co/api/v2/pokemon-species/{id}"
        descripcion_response = requests.get(descripcion_url)
        descripcion = descripcion_response.json()
        # Obtiene el flavor text
        flavor_text = descripcion["flavor_text_entries"]
        # Obtiene la descripcion en español
        descripcion_esp = [descripcion["flavor_text"] for descripcion in flavor_text if descripcion["language"]["name"] == "es"]
        resultado += f"\nDescripción: {descripcion_esp[0]}"
    else:
        resultado = "Pokemon no encontrado"
        # Elimina la imagen del label si no se encuentra el pokemon
        label_imagen.config(image=None)
    # Configura la etiqueta label para mostrar la información del pokemon
    label_resultado.config(text=resultado)

def limpiar():
    label_resultado.config(text="")
    label_imagen.config(image=None)
    label_imagen.image = None  # Añadido para asegurarse de que se elimina la referencia de la imagen

# Creamos la ventana principal de la aplicación
window = tk.Tk()
window.title("Pokedex")

# Cargar la imagen de fondo desde un archivo local
bg_image = Image.open("background.jpg")  # Reemplaza "background.jpg" con el nombre de tu archivo de imagen
bg_photo = ImageTk.PhotoImage(bg_image)

# Crear un label para la imagen de fondo
bg_label = tk.Label(window, image=bg_photo)
bg_label.place(relwidth=1, relheight=1)
bg_label.image = bg_photo  # Mantiene una referencia a la imagen

# Crear un frame para los botones en la parte superior
frame_botones = tk.Frame(window, bg='white')
frame_botones.pack(pady=10)

# Botón para buscar un Pokémon aleatorio
button_aleatorio = tk.Button(frame_botones, text="Pokemon Aleatorio", command=pokemon_aleatorio)
button_aleatorio.pack(side="left", padx=10)

# Botón para limpiar resultados e imágenes y refrescar la ventana
button_limpiar = tk.Button(frame_botones, text="Limpiar", command=limpiar)
button_limpiar.pack(side="left", padx=10)

# Crear un frame para la imagen y los datos
frame_info = tk.Frame(window, bg='white')
frame_info.pack(pady=20, padx=10)

# Una etiqueta para mostrar la imagen del Pokémon en el lado izquierdo
label_imagen = tk.Label(frame_info, bg='white')
label_imagen.grid(row=0, column=0, rowspan=2, padx=10)

# Crea una etiqueta vacía para mostrar los resultados a la derecha de la imagen
label_resultado = tk.Label(frame_info, text="", bg='white', justify="left")
label_resultado.grid(row=0, column=1, padx=10)

# Crear un frame para el entry y el botón "Buscar"
frame_entry = tk.Frame(window, bg='white')
frame_entry.pack(pady=10)

# Crear una entrada para recibir el nombre del Pokémon
entry_pokemon = tk.Entry(frame_entry)
entry_pokemon.pack(side="left", padx=10)

# Botón para buscar un Pokémon
button_buscar = tk.Button(frame_entry, text="Buscar", command=buscar_pokemon)
button_buscar.pack(side="left", padx=10)

# Inicia el bucle principal de la ventana
window.mainloop()

