from Controllers.CalculadoraComplejos import CalculadoraComplejos
from Controllers.ICalculadora import ICalculadora
from Models.Complejo import Complejo
from Models.VectorComplejo import VectorComplejo


class CalculadoraVectores(ICalculadora):
    def __init__(self):
        ICalculadora.__init__(self)
        self.calcComplejos = CalculadoraComplejos()

    def printOptions(self):
        print("1. Suma")
        print("2. Producto interno")
        print("3. Distancia entre vectores")
        print("4. Multiplicación por escalar")
        print("5. Inverso")
        print("6. Norma")

        num = int(input("Por favor digite el numero de la operación\n"))
        v1: VectorComplejo = \
            VectorComplejo(VectorComplejo.decode(input("Digite el vector separando cada componente por comas\n")))
        if num < 4:
            v2: VectorComplejo = \
                VectorComplejo(VectorComplejo.decode(input("Digite el vector 2 separando cada componente por comas\n")))
            if num == 1:
                print(self.sumVectores(v1, v2).get())
            elif num == 2:
                print(round(self.productoInterno(v1, v2), 2))
            elif num == 3:
                print(round(self.distancia(v1, v2), 2))
        elif num == 4:
            c = Complejo.decode(input("Digite el numero de la forma a + bi"))
            print(self.multVector(v1, c).get())
        elif num == 5:
            print(self.inversoVector(v1).get())
        elif num == 6:
            print(round(self.norma(v1), 2))
        else:
            Exception("Not valid option")

    def sumVectores(self, v1: VectorComplejo, v2: VectorComplejo) -> VectorComplejo:
        lista = []
        for i in range(len(v1.components)):
            lista.append(self.calcComplejos.sumComplex(v1.components[i], v2.components[i]))

        return VectorComplejo(lista)

    def getAdjunta(self, v1: VectorComplejo) -> VectorComplejo:
        lista = []
        for complejo in v1.components:
            lista.append(self.calcComplejos.conjugado(complejo))

        return VectorComplejo(lista)


    @staticmethod
    def inversoVector(v: VectorComplejo) -> VectorComplejo:
        lista = []
        for comp in v.components:
            lista.append(Complejo(comp.real*-1, comp.complejo * -1))
        return VectorComplejo(lista)

    def multVector(self, v: VectorComplejo, c: Complejo) -> VectorComplejo:
        lista = []
        for c1 in v.components:
            lista.append(self.calcComplejos.multComplex(c1, c))
        return VectorComplejo(lista)

    def productoInterno(self, v1: VectorComplejo, v2: VectorComplejo) -> float:
        producto = 0
        vAdj = self.getAdjunta(v1)
        for i in range(len(v1.components)):
            producto += self.calcComplejos.multComplex(vAdj.components[i], v2.components[i]).real
        return producto

    def norma(self, V: VectorComplejo) -> float:
        return self.productoInterno(V, V)**(1/2)

    def distancia(self, v1: VectorComplejo, v2: VectorComplejo) -> float:
        for c2 in v2.components:
            c2.real *= -1
            c2.complejo *= -1

        prd = self.productoInterno(self.sumVectores(v1, v2), self.sumVectores(v1, v2))
        return prd**(1/2)

