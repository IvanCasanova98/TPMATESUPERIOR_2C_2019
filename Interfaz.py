import tkinter
from tkinter import *
from tkinter import font, Tk, messagebox

from matplotlib.figure import Figure

import utils
from utils import Punto
import Interpolacion
from Interpolacion import *

master: Tk = Tk()
master.title("FINTER")
master.geometry('640x480')

metodo = Interpolacion(Lagrange())

puntos = []
x0 = StringVar()
y0 = StringVar()

fuente = font.Font(weight='bold')
tkinter.Label(master, text="X", font=fuente).place(x=240, y=0)
tkinter.Label(master, text="F(X)", font=fuente).place(x=360, y=0)

textX1 = tkinter.Entry(master, textvariable=x0)
textY1 = tkinter.Entry(master, textvariable=y0)
textX1.place(x=190, y=30)
textY1.place(x=320, y=30)


def formalizarlabellistasting(label, lista):
    return label + "  " + "  ".join(map(str, lista))


def crearlistai():
    global puntos
    i = 0;
    listai = []
    while i <= len(puntos) - 1:
        listai.append(i)
        i += 1
    return listai


Etiquetai = tkinter.Label(master, text=formalizarlabellistasting("i", crearlistai()), font=fuente)
Etiquetai.place(x=10, y=80)

EtiquetaX = tkinter.Label(master, text=formalizarlabellistasting("X", map(lambda p: p.x, puntos)), font=fuente)
EtiquetaX.place(x=10, y=100)
EtiquetaY = tkinter.Label(master, text=formalizarlabellistasting("F(x)", map(lambda p: p.y, puntos)), font=fuente)
EtiquetaY.place(x=10, y=120)

lagrange = IntVar()
NewtonGreg = IntVar()
checkNewGreg = tkinter.Checkbutton(master, text="Interpolación polinómica de Lagrange", variable=lagrange,
                                   state=DISABLED)
checkNewGreg.place(x=10, y=160)
checkLagrange = tkinter.Checkbutton(master, text="Interpolación polinómica Newton-Gregory", variable=NewtonGreg,
                                    state=DISABLED)
checkLagrange.place(x=10, y=180)


def agregarrpuntos():
    global puntos
    punto = Punto(int(x0.get()), int(y0.get()))
    puntos.append(punto)
    actualizarlista()


def deletearpuntos():
    global puntos
    punto = Punto(int(x0.get()), int(y0.get()))
    if punto in puntos:
        puntos.remove(punto)
        actualizarlista()
    else:
        messagebox.showinfo("Warning", "El punto no se encuentra en la lista")


def actualizarlista():
    global puntos
    puntos = utils.ordernarpuntos(puntos)
    solopuntosx = map(lambda p: p.x, puntos)
    print(*solopuntosx)
    textX1.delete(0, END)
    textY1.delete(0, END)
    actualizarlabelpuntos()
    if len(puntos) > 1:
        verificarequidistancia(puntos)
        activarCheckBox()


def activarCheckBox():
    global checkNewGreg
    global checkLagrange
    checkNewGreg['state'] = "normal"
    checkLagrange['state'] = "normal"


def actualizarlabelpuntos():
    global Etiquetai
    global EtiquetaY
    global EtiquetaX
    Etiquetai.config(text=formalizarlabellistasting("i       ", crearlistai()))
    EtiquetaX.config(text=formalizarlabellistasting("X     ", map(lambda p: p.x, puntos)))
    EtiquetaY.config(text=formalizarlabellistasting("F(X)", map(lambda p: p.y, puntos)))


def verificarequidistancia(listapuntos):
    if len(set(utils.diferenciaDeValoresLista(utils.puntosx(listapuntos)))) == 1:
        print("Los puntos son equidistantes")
    else:
        print("Los puntos no equidistan")


def calcular():
    metodo.calcularpolinomio(puntos)

Figure
tkinter.Button(master, text="Agregar Punto", command=agregarrpuntos).place(x=200, y=50)
tkinter.Button(master, text="Eliminar Punto", command=deletearpuntos).place(x=340, y=50)
botonCalcular = tkinter.Button(master, text="Calcular Polinomio", command=calcular, relief=GROOVE)
botonCalcular.place(x=15, y=260)
master.mainloop()
