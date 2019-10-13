from collections import namedtuple

from sympy import *
import numpy as np
import matplotlib.pyplot as plt

x, y, z = symbols('x y z')
init_printing(use_unicode=True)

Punto = namedtuple("Punto", "x y")


def diferenciaDeValoresLista(
        lista):  # este va a servir para la interpol newtown siempre devuelve una lista con len(# lista anterior) -1
    listanueva = []
    i = 0
    while i < len(lista) - 1:
        listanueva.append(int(lista[i]) - int(lista[i + 1]))
        i += 1
    return listanueva


def ordernarpuntos(puntos):
    return sorted(puntos, key=lambda tup: tup[0])


def puntosx(puntos):
    return list(map(lambda p: p.x, puntos))


def puntosy(puntos):
    return list(map(lambda p: p.y, puntos))


def entreParentesis(funcion):
    return "(" + funcion + ")"


def escribirpunto(x, xi):
    xicambiado = xi * -1
    if xi > 0:
        return entreParentesis(x + str(xicambiado))
    else:
        return entreParentesis(x + "+" + str(xicambiado))

def calcularLx(x, listaX):
    numerador = ""
    denominador = ""
    for puntox in listaX:
        if x != puntox:
            numerador += escribirpunto("x", puntox) + "*"
            denominador += escribirpunto(str(x), puntox) + "*"
    lx = entreParentesis(numerador[:-1]) + "/" + entreParentesis(denominador[:-1])
    return lx


def simplificarFuncion(funcion):
    print(expand(sympify(funcion)))
    return expand(sympify(funcion))


def pasarFuncionAPuntos(funcion, arrayPuntos):
    y = []
    for puntox in arrayPuntos:
        if puntox > 0:
            y.append(int(simplify(funcion.replace("x", entreParentesis(str(puntox))))))
        else:
            y.append(int(simplify(funcion.replace("x", entreParentesis(str(puntox))))))
    # map(lambda puntox: int(simplify(funcion.replace("x", str(puntox)))), arrayPuntos)
    print(*y)
    return y


def graficarPolinomio(funcion, puntosx, puntosy):
    rango = range(puntosx[0], puntosx[-1] * 5)
    x = rango
    y = pasarFuncionAPuntos(str(funcion), rango)
    plt.plot(x, y, 'r-', puntosx, puntosy, 'bs')
    plt.show()
