from Controllers.ICalculadora import ICalculadora
from Models.Complejo import Complejo
from Models.VectorComplejo import VectorComplejo



class CalculadoraVectores(ICalculadora):
    def __init__(self):
        ICalculadora.__init__(self)

    def printOptions(self):
        print("1. Suma")
        print("2. Producto interno")
        print("3. Distancia entre vectores")
        print("4. Multiplicación por escalar")
        print("5. Inverso")
        print("6. Norma")

        num = int(input("Por favor digite el numero de la operación\n"))
        v1: VectorComplejo = VectorComplejo.decode(input("Digite el vector separando cada componente por comas\n"))
        if num < 4:
            v2: VectorComplejo = VectorComplejo.decode(input("Digite el vector 2 separando cada componente por comas\n"))
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

    @staticmethod
    def sumVectores(v1: VectorComplejo, v2: VectorComplejo) -> VectorComplejo:
        # TODO
        pass

    @staticmethod
    def inversoVector(v: VectorComplejo) -> VectorComplejo:
        # TODO
        pass

    @staticmethod
    def multVector(v: VectorComplejo, c) -> VectorComplejo:
        # TODO
        pass

    @staticmethod
    def productoInterno(v1: VectorComplejo, v2: VectorComplejo) -> float:
        # TODO
        pass

    @staticmethod
    def norma(V: VectorComplejo) -> float:
        # TODO
        pass

    @staticmethod
    def distancia(v1: VectorComplejo, v2: VectorComplejo) -> float:
        # TODO
        pass
