import math

from Models.IComplejo import IComplejo


class Complejo(IComplejo):

    def __init__(self, n1: float, n2: float, isCartesiano=True):
        """
        :param n1: parte real o el valor de rho
        :param n2: parte compleja o el valor del angulo en grados
        :param isCartesiano: especifica si es cartesiano o no
        """
        IComplejo.__init__(self)
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

    def __eq__(self, other):
        areEquals = False
        if isinstance(other, Complejo) and self.real == other.real and self.complejo == other.complejo:
            areEquals = True

        return areEquals

    @staticmethod
    def decode(num: str):
        """
        convierte un string que posee un numero complejo escrito de forma cartesiana a un numero complejo
        :param num: es de la forma a +bi
        :return: Complejo()
        """
        aux = num.split()
        if 'i' in aux[1]:
            return Complejo(int(aux[0].strip()), int(aux[1][:len(aux[1])-1].strip()))
        else:
            return Complejo(int(aux[1].strip()), int(aux[0][:len(aux[0]) - 1].strip()))

    @staticmethod
    def recibaNum():
        return Complejo.decode(input("por favor digite el  numero de la forma a +bi\n"))

    def getCartesiano(self) -> str:
        """
        Retorna un string con el numero en corrdenadas cartesianas
        :return: el numero en coordenadas cartesianas
        """
        return "({0}, {1})".format(round(self.real, 2), round(self.complejo,2))

    def get(self) -> str:
        """
        Retorna un string con el numero en corrdenadas cartesianas pero mostrando la parte compleja
        :return: string con el numero
        """
        return "{0} {1}i".format(self.real, self.__getComplejo())

    def getPolar(self) -> str:
        """
        Retorna un string con el numero en corrdenadas polares
        :return: string con el numero
        """
        return "({0}, {1}°)".format(self.rho, self.angle)

    def getAngle(self) -> str:
        """
        Retorna un string con el angulo en grados.
        :return: string con el numero
        """
        return "{0}°".format(self.angle)

    def __getComplejo(self) -> str:
        """
        Retorna un string con la parte compleja del numero añadiendo su signo
        """
        if self.complejo > 0:
            return '+{0}'.format(self.complejo)
        else:
            return str(self.complejo)

    def __calculateAngle(self) -> float:
        """
        Calcula el valor del angulo cuando se tiene el numero en coordenadas cartesianas
        """
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

    def __calculateModulo(self) -> float:
        """
        Calcula el valor del modulo del numero
        """
        return ((self.real ** 2) + (self.complejo ** 2)) ** 0.5

