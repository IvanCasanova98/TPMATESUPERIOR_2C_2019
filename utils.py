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
        listanueva.append(int(lista[i + 1]) - int(lista[i]))
        i += 1
    return listanueva


def diferenciaDeValoresListaNewtonLagrange(
        lista, puntosx, salto):  # este va a servir para la interpol newtown siempre devuelve una lista con len(# lista
    # anterior) -1
    listanueva = []
    i = 0
    while i < len(lista) - 1:
        if (puntosx[salto]) - (puntosx[i]) == 0:
            listanueva.append(0)
        else:
            listanueva.append(((lista[i + 1]) - (lista[i])) / ((puntosx[salto]) - (puntosx[i])))
        i += 1
        salto += 1
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


def calcularTandaPuntos(listaPuntos):
    Tanda = ""
    for punto in listaPuntos:
        Tanda += escribirpunto("x", punto) + "*"

    return Tanda[:-1]


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


def calcularGradoPolinomio(funcion):
    pow = '**'
    if str(funcion).find(pow)!=-1:
        return str(funcion[funcion.find(pow)+2])
    if "x" in funcion:
        return '1'
    return '0'


def ParsearALx(lista):
    i=0
    listaNueva=[]
    while i < len(lista):
        listaNueva.append("LX " + str(i) + " = "+ lista[0])
        i+=1
    return listaNueva

