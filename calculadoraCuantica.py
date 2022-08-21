import math


class Complejo:
    def __init__(self, n1: float, n2: float, isCartesiano=True):
        """
        :param n1: parte real o el valor de rho
        :param n2: parte compleja o el valor del angulo en grados
        :param isCartesiano: especifica si es cartesiano o no
        self.__real
        self.__complejo
        self.__modulo
        self.__angle
        """

        if isCartesiano:
            self.real = n1
            self.complejo = n2
            self.modulo = self.__calculateModulo()
            self.angle = self.__calculateAngle()
            self.rho = self.modulo
        else:
            self.rho = n1
            self.angle = n2
            self.real = self.rho*math.cos(self.angle*math.pi/180)
            self.complejo = self.rho * math.sin(self.angle * math.pi / 180)
            self.modulo = self.__calculateModulo()

    @staticmethod
    def decode(num: str):
        """
        :param num: es de la forma a +bi
        :return:
        """
        aux = num.split()
        if 'i' in aux[1]:
            return Complejo(int(aux[0].strip()), int(aux[1][:len(aux[1])-1].strip()))
        else:
            return Complejo(int(aux[1].strip()), int(aux[0][:len(aux[0]) - 1].strip()))

    def getCartesiano(self):
        return "({0}, {1})".format(round(self.real, 2), round(self.complejo,2))

    def get(self):
        return "{0} {1}i".format(self.real, self.__getComplejo())

    def getPolar(self):
        return "({0}, {1}°)".format(self.rho, self.angle)

    def getAngle(self):
        return "{0}°".format(self.angle)

    def __getComplejo(self):
        if self.complejo > 0:
            return '+{0}'.format(self.complejo)
        else:
            return str(self.complejo)

    def __calculateAngle(self):
        if self.real != 0:
            num = round(math.atan2(self.complejo, self.real)*57.3, 2)
            if self.complejo < 0:
                if self.real < 0:
                    num += 180
                elif self.real > 0:
                    num = 360 - num
            return num
        else:
            return None

    def __calculateModulo(self):
        return ((self.real ** 2) + (self.complejo ** 2)) ** 0.5


def sumComplex(n1: Complejo, n2: Complejo) -> Complejo:
    return Complejo(n1.real + n2.real, n1.complejo + n2.complejo)


def restComplex(n1: Complejo, n2: Complejo) -> Complejo:
    return Complejo(n1.real - n2.real, n1.complejo - n2.complejo)


def multComplex(n1: Complejo, n2: Complejo) -> Complejo:
    real = (n1.real * n2.real) + (n1.complejo * n2.complejo * -1)
    decimal = (n1.real * n2.complejo) + (n1.complejo * n2.real)
    return Complejo(real, decimal)


def divComplex(n1: Complejo, n2: Complejo) -> Complejo or None:
    denominador = (n2.real**2) + (n2.complejo**2)
    if denominador != 0:
        real = ((n1.real*n2.real) + (n1.complejo*n2.complejo))/denominador
        complejo = ((n2.real*n1.complejo) - (n1.real*n2.complejo))/denominador
        return Complejo(real, complejo)
    else:
        return None


def toPolar(a: Complejo):
    return a.getPolar()
    pass


def toCartesianas(a: Complejo):
    return a.getCartesiano()


def conjugado(a: Complejo) -> Complejo:
    return Complejo(a.real, a.complejo*-1)


def getFase(a: Complejo):
    return round(a.angle, 2)


def multMatrices(A, B):
    C = [[0, 0], [0, 0]]
    for i in range(len(A)):
        for j in range(len(A[0])):
            for k in range(len(A[0])):
                C[i][j] += A[i][k]*B[k][j]
    return C


def printOptions():
    print("1. Suma")
    print("2. resta")
    print("3. Producto")
    print("4. división")
    print("5. modulo")
    print("6. Conjugado")
    print("7. Convertir a polares")
    print("8. Convertir a cartesianas")
    print("9. Fase")


def test():
    c1 = Complejo(5, -10)
    c2 = Complejo(-2, 13)
    rta = sumComplex(c1, c2)
    assert(rta.real == 3)
    assert(rta.complejo == 3)
    rta = restComplex(c1, c2)
    assert(rta.real == 7)
    assert(rta.complejo == -23)
    rta = multComplex(c1, c2)
    assert(rta.real == 120)
    assert(rta.complejo == 85)
    c1 = Complejo(-2, 1)
    c2 = Complejo(1, 2)
    rta = divComplex(c1, c2)
    assert(rta.real == 0)
    assert(rta.complejo == 1)
    assert(c1.modulo == 5**0.5)
    assert(c2.modulo == 5**0.5)
    assert(rta.modulo == 1.0)
    rta = conjugado(c1)
    assert(rta.complejo == -1)
    assert(getFase(c2) > 62 and getFase(c2) < 65)


def main():
    print("Calculadora cuantica, bienvenido.")
    printOptions()
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
            print(sumComplex(c1, c2).get())
        elif num == 2:
            print(restComplex(c1, c2).get())
        elif num == 3:
            print(multComplex(c1, c2).get())
        elif num == 4:
            print(divComplex(c1, c2).get())
        else:
            print("Operación invalida. Se reiniciará el programa.")
            main()
    elif num == 5:
        print(c1.modulo)
    elif num == 6:
        print(conjugado(c1).get())
    elif num == 7:
        print(c1.getPolar())
    elif num == 8:
        print(c1.getCartesiano())
    elif num == 9:
        print(c1.getAngle())
    else:
        print("Operación invalida. Se reiniciará el programa.")
        main()


main()
