from abc import abstractmethod, ABC
import utils
from utils import Punto


class Metodo(ABC):
    @abstractmethod
    def calcular(self, puntos):
        pass


class Lagrange(Metodo):
    def calcular(self, puntos):
        puntosx= utils.puntosx(puntos)
        puntosy=utils.puntosy(puntos)
        multiplicadoresDeLagrange = []
        for punto in puntosx:
            multiplicadoresDeLagrange.append(utils.calcularLx(punto, puntosx))
        Polinomio ="+".join(map(lambda lx, y: str(y)+"*"+lx, multiplicadoresDeLagrange,puntosy))
        print(Polinomio)
        PolinomioSimplificado=utils.simplificarFuncion(Polinomio)
        utils.graficarPolinomio(PolinomioSimplificado, puntosx,puntosy)


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






