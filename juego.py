from defi import *
import random as rd

numeros = []
vidas = 5
puntaje = 100
racha = 0

for i in range(12):
    numeros.append(rd.randint(1,10))

print("Indique su RUT")
run = input(">> ")

print("Indique su nombre")
nom = input(">> ")

print("Este es el prototipo de un juego.\nAdivine todos los numeros en la lista y gane una recompensa.\nTiene 5 vidas para realizarlo")

vidas, puntaje = encontrarNum(numeros, vidas, puntaje, racha)

informacionJugador = {

    "Rut": run,
    "Nombre": nom.capitalize(),
    "Numeros faltantes": [i for i in numeros],
    "Puntaje": puntaje

}

print("\nResultados:")
for i, b, in informacionJugador.items():
    print(f"{i}: {b}")