from Models.Complejo import Complejo
from Controllers.ICalculadora import ICalculadora


class CalculadoraComplejos(ICalculadora):
    def __init__(self):
        ICalculadora.__init__(self)

    def printOptions(self):
        print("1. Suma")
        print("2. resta")
        print("3. Producto")
        print("4. división")
        print("5. modulo")
        print("6. Conjugado")
        print("7. Convertir a polares")
        print("8. Convertir a cartesianas")
        print("9. Fase")
        num = int(input("Por favor digite el numero de la operación\n"))
        c1: Complejo
        if num != 8:
            c1 = Complejo.decode(input("por favor digite el  numero de la forma a +bi\n"))
        else:
            data = input("Digite el numero de la forma rho, angulo. El angulo se lee en grados\n ").split()
            c1 = Complejo(int(data[0]), int(data[1]), isCartesiano=False)

        if num < 5:
            c2: Complejo = Complejo.decode(input("por favor digite el otro numero de la forma a +bi\n"))
            if num == 1:
                print(self.sumComplex(c1, c2).get())
            elif num == 2:
                print(self.restComplex(c1, c2).get())
            elif num == 3:
                print(self.multComplex(c1, c2).get())
            elif num == 4:
                print(self.divComplex(c1, c2).get())
        elif num == 5:
            print(c1.modulo)
        elif num == 6:
            print(self.conjugado(c1).get())
        elif num == 7:
            print(c1.getPolar())
        elif num == 8:
            print(c1.getCartesiano())
        elif num == 9:
            print(c1.getAngle())
        else:
            Exception("Not valid option")

    @staticmethod
    def sumComplex(n1: Complejo, n2: Complejo) -> Complejo:
        return Complejo(n1.real + n2.real, n1.complejo + n2.complejo)

    @staticmethod
    def restComplex(n1: Complejo, n2: Complejo) -> Complejo:
        return Complejo(n1.real - n2.real, n1.complejo - n2.complejo)

    @staticmethod
    def multComplex(n1: Complejo, n2: Complejo) -> Complejo:
        real = (n1.real * n2.real) + (n1.complejo * n2.complejo * -1)
        decimal = (n1.real * n2.complejo) + (n1.complejo * n2.real)
        return Complejo(real, decimal)

    @staticmethod
    def divComplex(n1: Complejo, n2: Complejo) -> Complejo or None:
        denominador = (n2.real ** 2) + (n2.complejo ** 2)
        if denominador != 0:
            real = ((n1.real * n2.real) + (n1.complejo * n2.complejo)) / denominador
            complejo = ((n2.real * n1.complejo) - (n1.real * n2.complejo)) / denominador
            return Complejo(real, complejo)
        else:
            return None

    @staticmethod
    def toPolar(a: Complejo):
        return a.getPolar()
        pass

    @staticmethod
    def toCartesianas(a: Complejo):
        return a.getCartesiano()

    @staticmethod
    def conjugado(a: Complejo) -> Complejo:
        return Complejo(a.real, a.complejo * -1)

    @staticmethod
    def getFase(a: Complejo):
        return round(a.angle, 2)


