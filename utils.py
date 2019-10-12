from collections import namedtuple

Punto = namedtuple("Punto", "x y")


def diferenciaDeValoresLista(lista):  # este va a servir para la interpol newtown siempre devuelve una lista con len(# lista anterior) -1
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


def escribirpunto(x, xi):
    xicambiado = xi * -1
    return "(" + x + str(xicambiado) + ")"
