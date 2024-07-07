"""
3.1.2 Actividad listas (Clase 1)
Ejercicio 4
4) Cree un menú para registrar usuarios e iniciar sesión, también el menú tendrá la
opción de eliminar usuarios, para ello, utilice el nombre de usuario, además para
confirmar la eliminación, deberán escribir la contraseña correspondiente de cada
usuario.
1. Inicio sesión.
2. Registrar usuario
3. Eliminar usuario.
4. Salir.
La opción 1 solo mostrará un mensaje exitoso si ha iniciado correctamente, o un error de caso contrario.
"""
# Función para registrar usuario
def registrar_usuario(usuarios):
    # Solicitar nombre de usuario
    nombre_usuario = input("Ingrese el nombre de usuario: ")
    # Solicitar contraseña
    contrasena = input("Ingrese la contraseña: ")
    # Agregar usuario a la lista de usuarios
    usuarios.append({"nombre_usuario": nombre_usuario, "contrasena": contrasena})
    print("Usuario registrado correctamente")

# Función para eliminar usuario
def eliminar_usuario(usuarios):
    # Solicitar nombre de usuario
    nombre_usuario = input("Ingrese el nombre de usuario: ")
    # Solicitar contraseña
    contrasena = input("Ingrese la contraseña: ")
    # Buscar usuario
    usuario_encontrado = False
    for usuario in usuarios:
        if usuario["nombre_usuario"] == nombre_usuario:
            usuario_encontrado = True
            if usuario["contrasena"] == contrasena:
                # Eliminar usuario
                usuarios.remove(usuario)
                print("Usuario eliminado correctamente")
                break
            else:
                print("Contraseña incorrecta")
                break
    if usuario_encontrado == False:
        print("Usuario no encontrado")

# Función para iniciar sesión
def iniciar_sesion(usuarios):
    # Solicitar nombre de usuario
    nombre_usuario = input("Ingrese el nombre de usuario: ")
    # Solicitar contraseña
    contrasena = input("Ingrese la contraseña: ")
    # Buscar usuario
    usuario_encontrado = False
    for usuario in usuarios:
        if usuario["nombre_usuario"] == nombre_usuario:
            usuario_encontrado = True
            if usuario["contrasena"] == contrasena:
                print("Inicio de sesión correcto")
                break
            else:
                print("Contraseña incorrecta")
                break
    if usuario_encontrado == False:
        print("Usuario no encontrado")

# Menú
usuarios = []
while True:
    print("1. Iniciar sesión.")
    print("2. Registrar usuario.")
    print("3. Eliminar usuario.")
    print("4. Salir.")
    opcion = input("Seleccione una opción: ")
    if opcion == "1":
        iniciar_sesion(usuarios)
    elif opcion == "2":
        registrar_usuario(usuarios)
    elif opcion == "3":
        eliminar_usuario(usuarios)
    elif opcion == "4":
        break
    else:
        print("Opción no válida")

