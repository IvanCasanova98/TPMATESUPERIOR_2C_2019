import tkinter
from tkinter import *
from tkinter import font, Tk, messagebox
import matplotlib as plt

plt.use("TkAgg")
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.figure import Figure
from Interpolacion import *

master: Tk = Tk()
master.title("FINTER")
master.geometry('680x480')

metodo = Interpolacion(Lagrange())

puntos = []
x0 = StringVar()
y0 = StringVar()

fuente = font.Font(weight='bold')
tkinter.Label(master, text="X", font=fuente).place(x=240, y=0)
labelFunction = tkinter.Label(master, text="", font=fuente)
labelFunction.place(x=300, y=160)
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


def actualizarCheckLagra():
    global checkNewGreg
    global checkRegresivo
    global checkProgresivo
    global checkLagrange
    global metodo
    checkLagrange.select()
    checkProgresivo.deselect()
    checkRegresivo.deselect()
    checkProgresivo['state'] = DISABLED
    checkRegresivo['state'] = DISABLED
    checkNewGreg.deselect()
    metodo = Interpolacion(Lagrange())


def actualizarCheckNewGreg():
    global checkLagrange
    global checkRegresivo
    global checkProgresivo
    global checkNewGreg
    global metodo
    checkNewGreg.select()
    checkProgresivo.select()
    checkProgresivo['state'] = NORMAL
    checkRegresivo['state'] = NORMAL
    checkLagrange.deselect()
    checkRegresivo.deselect()
    metodo = Interpolacion(NewtonGregoryProgre())


def actualizarCheckProgre():
    global checkRegresivo
    global checkProgresivo
    global metodo
    checkProgresivo.select()
    checkRegresivo.deselect()
    metodo = Interpolacion(NewtonGregoryProgre())

def actualizarCheckRegre():
    global checkRegresivo
    global checkProgresivo
    global metodo
    checkProgresivo.deselect()
    checkRegresivo.select()
    metodo = Interpolacion(NewtonGregoryRegre())


progresivo = IntVar()
regresivo = IntVar()
lagrange = IntVar()
NewtonGreg = IntVar()

checkLagrange = tkinter.Checkbutton(master, text="Interpolación polinómica de Lagrange", variable=lagrange,
                                    state=DISABLED, command=actualizarCheckLagra)
checkLagrange.place(x=10, y=160)

checkNewGreg = tkinter.Checkbutton(master, text="Interpolación polinómica Newton-Gregory", variable=NewtonGreg,
                                   state=DISABLED, command=actualizarCheckNewGreg)
checkNewGreg.place(x=10, y=180)
checkProgresivo = tkinter.Checkbutton(master, text="Progresivo", variable=progresivo,
                                      state=DISABLED, command=actualizarCheckProgre)
checkProgresivo.place(x=30, y=200)
checkRegresivo = tkinter.Checkbutton(master, text="Regresivo", variable=regresivo,
                                     state=DISABLED, command=actualizarCheckRegre)
checkRegresivo.place(x=30, y=220)


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
    if len(puntos) >= 1:
        verificarequidistancia(puntos)
        activarCheckBox()


def activarCheckBox():
    global checkNewGreg
    global checkLagrange
    checkNewGreg['state'] = "normal"
    checkLagrange['state'] = "normal"
    actualizarCheckLagra() 



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


def graficarPolinomio(funcion, puntosx, puntosy):
    global labelFunction
    rango = range(puntosx[0] * -5, puntosx[-1] * 5)
    f = Figure(figsize=(4, 3), dpi=100)
    x = rango
    y = utils.pasarFuncionAPuntos(str(funcion), rango)
    a = f.add_subplot(111)
    a.plot(x, y, 'r-', puntosx, puntosy, 'rs')
    a.grid(linestyle='-', linewidth=1)
    canvas = FigureCanvasTkAgg(f, master)
    canvas.draw()
    canvas.get_tk_widget().place(x=10, y=30)
    canvas._tkcanvas.place(x=290, y=180)
    labelFunction["text"] = "Funcion hallada: " + str(funcion)


def calcular():
    funcion = metodo.calcularpolinomio(puntos)
    graficarPolinomio(funcion, utils.puntosx(puntos), utils.puntosy(puntos))

Figure
tkinter.Button(master, text="Agregar Punto", command=agregarrpuntos).place(x=200, y=50)
tkinter.Button(master, text="Eliminar Punto", command=deletearpuntos).place(x=340, y=50)
botonCalcular = tkinter.Button(master, text="Calcular Polinomio", command=calcular, relief=GROOVE)
botonCalcular.place(x=15, y=260)
master.mainloop()
