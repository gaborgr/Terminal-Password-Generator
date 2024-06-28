import random


def generar_contrasena(longitud):
    caracteres = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNÑOPQRSTUVWXYZ0123456789@!$%&/()=?¡[];:"
    contrasena = ""
    for i in range(longitud):
        contrasena += random.choice(caracteres)
    return contrasena


longitud = int(input("Cual es la longitd de la contraseña: "))

nueva_contrasena = generar_contrasena(longitud)

print("La nueva contraseña es: ", nueva_contrasena)
