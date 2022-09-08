from Models.Complejo import Complejo
from Models.VectorComplejo import VectorComplejo
from Models.IComplejo import IComplejo


class MatrizCompleja(IComplejo):
    @staticmethod
    def recibaNum():
        return MatrizCompleja(list())

    @staticmethod
    def decode(item: str) -> list[VectorComplejo]:
        sComplejos = item.split('|')
        complejos: list[VectorComplejo] = []
        for complejo in sComplejos:
            complejos.append(VectorComplejo(VectorComplejo.decode(complejo.strip())))
        return complejos

    def __init__(self, components: list[VectorComplejo]):
        IComplejo.__init__(self)
        self.components = components

    def __len__(self):
        return len(self.components[0])

    def __eq__(self, other):
        areEquals = True
        if isinstance(other, MatrizCompleja) and self.getDimensions() == other.getDimensions():
            for i in range(len(self.components)):
                if self.components[i] != other.components[i]:
                    areEquals = False
                    break
        else:
            areEquals = False

        return areEquals

    def get(self):
        for j in range(len(self)):
            for i in range(len(self.components)):
                print(self.components[i].getComplejo(j).get(), end="  ")
            print()

    def isSquare(self):
        return len(self.components[0]) == len(self.components)

    def getPos(self, i, j) -> Complejo:
        return self.components[j].getComplejo(i)

    def setPos(self, i, j, value):
        self.components[j].setPos(i, value)

    def getDimensions(self):
        return [len(self.components[0]), len(self.components)]

