def validarInt(a):

    while True:

        try:

            return int(a)

        except ValueError:

            print("Intente nuevamente")
            a = input(">> ")

def encontrarNum(numeros, vidas, puntaje, racha):

    while vidas > 0 and len(numeros) > 0:

        print(f"Vidas Restantes: {vidas}")
        print(f"Numeros restantes: {len(numeros)}")

        a = input(">> ")
        b = validarInt(a)

        if b in numeros:
            numeros.remove(b)

            racha += 1
            puntaje *= racha
            
            print("¡Adivinaste un número!")
            print("Inserta otro")

        else:
            print("Te has equivocado")
            vidas -= 1
            racha = 0

    if vidas == 0:
        print("Has perdido todas tus vidas")
    else:
        print("Felicidades, has ganado el juego")

    return vidas, puntaje