from VectorComplejo import VectorComplejo
from Models.IComplejo import IComplejo


class MatrizCompleja(IComplejo):
    @staticmethod
    def decode(item: str) -> list[VectorComplejo]:
        sComplejos = item.split(',')
        complejos: list[VectorComplejo] = []
        for complejo in sComplejos:
            complejos.append(VectorComplejo(VectorComplejo.decode(complejo.strip())))
        return complejos

    def __init__(self, components: list[VectorComplejo]):
        IComplejo.__init__(self)
        self.components = components

    def get(self):
        print("[")
        for item in self.components:
            print(item.get())
        print("]")

    def isUnitaria(self) -> bool:
        # TODO
        pass

    def isHermitiana(self) -> bool:
        # TODO
        pass