import math
from Punto import Punto
import os


def graficar(matriz, puntos):
    for punto in puntos:
        x, y = punto.ajustar()
        matriz[y][x] = "*"


def mat():
    matriz = []
    for i in range(140):
        aux = []
        for j in range(340):
            if i == 10:
                aux.append("-")
            elif j == 1:
                aux.append("|")
            else:
                aux.append(" ")
        matriz.append(aux)
    return matriz


def evaluar(iteraciones, x):
    resultado = 0.25
    for i in range(1, iteraciones + 1):
        a, b = ((i * math.pi) / 2), (i * x)
        resultado += (1 / (math.pi * i)) * ((math.sin(a) * math.cos(b)) + (math.sin(b) * (1 - math.cos(a))))
    return resultado


def calcular(iteraciones):
    puntos = []
    for i in range(315):
        x = (i / 100)
        puntos.append(Punto(x, evaluar(iteraciones, x)))
    return puntos


def main():
    print("Serie de Fourier de una Onda Cuadrada\n")
    puntos = calcular(int(input("Ingresa el numero de iteraciones: ")))
    matriz = mat()
    graficar(matriz, puntos)
    matriz.reverse()
    os.system("clear")
    for fila in matriz:
        for celda in fila:
            print(celda, end="")
        print()


if __name__ == '__main__':
    main()
