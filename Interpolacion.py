from abc import abstractmethod, ABC
import utils


class Metodo(ABC):
    historia = []

    @abstractmethod
    def calcular(self, puntos):
        return
        pass

    @abstractmethod
    def definicionPhoto(self):
        return
        pass

    def _historia(self):
        return self.historia


class Lagrange(Metodo):

    def calcular(self, puntos):

        puntosx = utils.puntosx(puntos)
        puntosy = utils.puntosy(puntos)
        if len(puntosx) == 1:
            return puntosy[0]
        multiplicadoresDeLagrange = []
        for punto in puntosx:
            multiplicadoresDeLagrange.append(utils.calcularLx(punto, puntosx))
        self.historia.append(utils.ParsearALx(multiplicadoresDeLagrange))
        Polinomio = "+".join(map(lambda lx, y: str(y) + "*" + lx, multiplicadoresDeLagrange, puntosy))
        self.historia.append(Polinomio)
        self.historia.append(utils.simplificarFuncion(Polinomio))
        return utils.simplificarFuncion(Polinomio)

    def definicionPhoto(self):
        return "Lagrange.gif"


class NewtonGregoryProgre(Metodo):
    def calcular(self, puntos):
        puntosx = utils.puntosx(puntos)
        puntosy = utils.puntosy(puntos)
        if len(puntosx) == 1:
            return puntosy[0]
        i = 0
        ListasDiferencias = [puntosy]
        while i < len(puntosx) - 1:
            ListasDiferencias.append(utils.diferenciaDeValoresListaNewtonLagrange(ListasDiferencias[i], puntosx, i + 1))
            i += 1
        self.historia.append(utils.ParsearAΔ(ListasDiferencias))
        PrimerosValores = list(map(lambda listaDiferencia: listaDiferencia[0], ListasDiferencias))
        i = 1
        Polinomio = str(PrimerosValores[0]) + "+"
        while i < len(PrimerosValores):
            Polinomio += str(PrimerosValores[i]) + "*" + utils.calcularTandaPuntos(puntosx[:i]) + "+"
            i += 1
        self.historia.append(Polinomio[:-1])
        self.historia.append(utils.simplificarFuncion(Polinomio[:-1]))
        return utils.simplificarFuncion(Polinomio[:-1])

    def definicionPhoto(self):
        return "NewtonGregory.gif"


class NewtonGregoryRegre(Metodo):
    def calcular(self, puntos):

        puntosx = utils.puntosx(puntos)
        puntosy = utils.puntosy(puntos)
        if len(puntosx) == 1:
            return puntosy[0]
        i = 0
        ListasDiferencias = [puntosy]
        while i < len(puntosx) - 1:
            ListasDiferencias.append(utils.diferenciaDeValoresListaNewtonLagrange(ListasDiferencias[i], puntosx, i + 1))
            i += 1
        # print(*ListasDiferencias)
        self.historia.append(utils.ParsearAΔ(ListasDiferencias))
        print(*ListasDiferencias)
        UltimosValores = list(map(lambda listaDiferencia: listaDiferencia[-1], ListasDiferencias))
        i = 1
        Polinomio = str(UltimosValores[0]) + "+"
        puntosx.reverse()
        while i < len(UltimosValores):
            Polinomio += str(UltimosValores[i]) + "*" + utils.calcularTandaPuntos(puntosx[:i]) + "+"
            i += 1
        self.historia.append(Polinomio[:-1])
        self.historia.append(utils.simplificarFuncion(Polinomio[:-1]))
        return utils.simplificarFuncion(Polinomio[:-1])

    def definicionPhoto(self):
        return "NewtonGregory.gif"


class Interpolacion():
    polinomio = ""

    def __init__(self, strategy: Metodo) -> None:
        self._strategy = strategy

    @property
    def strategy(self) -> Metodo:
        return self._strategy

    @strategy.setter
    def strategy(self, strategy: Metodo) -> None:
        self._strategy = strategy

    def calcularpolinomio(self, puntos) -> None:
        self.polinomio = self._strategy.calcular(puntos)
