import string

alfabeto = list(string.ascii_lowercase)

#cambiar la ubicacion del diccionario, esto depende de la direccion en que lo haya guardado (debes modificar la direccion)
def cargar_diccionario():
   with open("diccionario.txt", "r", encoding="utf-8") as archivo:
        return archivo.readlines()

def buscar_en_diccionario(palabra, diccionario):
    return palabra + "\n" in diccionario

def descifrar_frase(frase, clave):
    frase_descifrada = ""
    clave = clave % 26
    for letra in frase.lower():
        if letra in alfabeto:
            indice = alfabeto.index(letra)
            indice -= clave 
            if indice < 0:
                indice += 26
            frase_descifrada += alfabeto[indice]
        else:
            frase_descifrada += letra 
    return frase_descifrada

print("========= CIFRADO CESAR ==========")

while True:
    print("1. Codificador ")
    print("2. Decodificar")
    print("3. Cracker")
    print("4. Salir")
    eleccion = int(input("Ingrese una opción para continuar: "))

    if eleccion == 1:
        mensaje = input("Ingrese un mensaje:  ")
        clave = int(input("Ingrese un número para cifrar el mensaje:  "))
        mensaje_cifrado = ""
        clave = clave % 26
        for letra in mensaje.lower():
            if letra in alfabeto:
                indice = alfabeto.index(letra)
                indice += clave 
                if indice >= 26:
                    indice -= 26
                mensaje_cifrado += alfabeto[indice]
            else:
                mensaje_cifrado += letra
        print("Mensaje cifrado:", mensaje_cifrado)
    
    elif eleccion == 2:
        mensaje = input("Ingrese un mensaje a descifrar:  ")
        clave = int(input("Ingrese un número para descifrar el mensaje:  ")) 
        mensaje_descifrado = descifrar_frase(mensaje, clave)
        print("Mensaje descifrado:", mensaje_descifrado)

    elif eleccion == 3:
        frase = input("Ingrese una frase para descifrar: ")
        diccionario = cargar_diccionario()
        print("Descifrando la frase:")
        mejor_puntuacion = -1
        frase_descifrada = ""
        mejor_clave =None
        for clave in range(26):
            frase_descifrada_actual = descifrar_frase(frase, clave)
            palabras_descifradas = frase_descifrada_actual.split()
            puntuacion = sum(buscar_en_diccionario(palabra, diccionario) for palabra in palabras_descifradas)
            if puntuacion > mejor_puntuacion:
                mejor_puntuacion = puntuacion
                frase_descifrada = frase_descifrada_actual
                mejor_clave = clave

        if frase_descifrada:
            print("Frase descifrada:", frase_descifrada)
            print("Clave utilizada:", mejor_clave)
        else:
            print("Ninguna opción es correcta. No todas las palabras están en el diccionario.")



    elif eleccion == 4:
        print("¡Hasta luego!")
        break

    else:
        print("Error: La opción ingresada no es válida.")
