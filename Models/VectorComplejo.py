from Models.Complejo import Complejo
from Models.IComplejo import IComplejo


class VectorComplejo(IComplejo):

    def __init__(self, components: list[Complejo or None]):
        IComplejo.__init__(self)
        self.components: list[Complejo] = components

    def __len__(self):
        return len(self.components)

    def __eq__(self, other):
        areEquals = True
        if isinstance(other, VectorComplejo) and len(self) == len(other):
            for i in range(len(self)):
                if self.components[i] != other.components[i]:
                    areEquals = False
                    break
        else:
            areEquals = False

        return areEquals

    @staticmethod
    def decode(item: str) -> list[Complejo]:
        sComplejos = item.split(',')
        complejos: list[Complejo] = []
        for complejo in sComplejos:
            complejos.append(Complejo.decode(complejo.strip()))
        return complejos

    @staticmethod
    def recibaNum(num=0):
        if num == 0:
            v = VectorComplejo.decode(input("Digite el vector separando cada componente por comas\n"))
        else:
            v = VectorComplejo.decode(input("Digite el vector {} separando cada componente por comas\n").format(num))
        return v

    def get(self):
        print("[")
        for item in self.components:
            print("({0})".format(item.get()), end=" ")
        print("]")

    def getComplejo(self, pos) -> Complejo:
        return self.components[pos]

    def setPos(self, pos: int, value: Complejo):
        self.components[pos] = value
