from abc import abstractmethod, ABC
import utils
from utils import Punto


class Metodo(ABC):
    @abstractmethod
    def calcular(self, puntos):
        return
        pass


class Lagrange(Metodo):
    def calcular(self, puntos):
        puntosx = utils.puntosx(puntos)
        puntosy = utils.puntosy(puntos)
        if len(puntosx) == 1:
            return puntosy[0]
        multiplicadoresDeLagrange = []
        for punto in puntosx:
            multiplicadoresDeLagrange.append(utils.calcularLx(punto, puntosx))
        Polinomio = "+".join(map(lambda lx, y: str(y) + "*" + lx, multiplicadoresDeLagrange, puntosy))
        print(Polinomio)
        return utils.simplificarFuncion(Polinomio)

class NewtonGregoryProgre(Metodo):
    def calcular(self,puntos):
        puntosx = utils.puntosx(puntos)
        puntosy = utils.puntosy(puntos)
        if len(puntosx) == 1:
            return puntosy[0]
        i =0
        ListasDiferencias=[puntosy]
        while i < len(puntosx)-1:
            ListasDiferencias.append(utils.diferenciaDeValoresListaNewtonLagrange(ListasDiferencias[i],puntosx,i+1))
            #faltadividir cuando no son equidistantes
            i += 1
        print(*ListasDiferencias)
        PrimerosValores = list(map(lambda listaDiferencia: listaDiferencia[0], ListasDiferencias))
        i=1
        Polinomio= str(PrimerosValores[0]) + "+"
        while i < len(PrimerosValores):
            Polinomio += str(PrimerosValores[i]) + "/"+ str(i)+ "*" + utils.calcularTandaPuntos(puntosx[:i]) + "+"
            i += 1
        print(Polinomio[:-1])
        return utils.simplificarFuncion(Polinomio[:-1])


class NewtonGregoryRegre(Metodo):
    def calcular(self,puntos):
        return 1



class Interpolacion():

    def __init__(self, strategy: Metodo) -> None:
        self._strategy = strategy

    @property
    def strategy(self) -> Metodo:
        return self._strategy

    @strategy.setter
    def strategy(self, strategy: Metodo) -> None:
        self._strategy = strategy

    def calcularpolinomio(self, puntos) -> None:
        return self._strategy.calcular(puntos)
