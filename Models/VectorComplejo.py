from Models.Complejo import Complejo
from Models.IComplejo import IComplejo


class VectorComplejo(IComplejo):

    @staticmethod
    def decode(item: str) -> list[Complejo]:
        sComplejos = item.split(',')
        complejos: list[Complejo] = []
        for complejo in sComplejos:
            complejos.append(Complejo.decode(complejo.strip()))
        return complejos

    def __init__(self, components: list[Complejo]):
        IComplejo.__init__(self)
        self.components = components

    def get(self):
        print("[")
        for item in self.components:
            print("({0})".format(item.get()), end=" ")
        print("]")

