from Controllers.ICalculadora import ICalculadora
from Models.MatrizCompleja import MatrizCompleja
from Models.VectorComplejo import VectorComplejo


class CalculadoraMatrices(ICalculadora):
    def __init__(self):
        ICalculadora.__init__(self)

    def printOptions(self):
        # TODO
        pass

    @staticmethod
    def sumMatrices(A: MatrizCompleja, B: MatrizCompleja) -> MatrizCompleja:
        # TODO
        pass

    @staticmethod
    def inversaMatriz(A: MatrizCompleja) -> MatrizCompleja:
        # TODO
        pass

    @staticmethod
    def multMatriz(A: MatrizCompleja, c) -> MatrizCompleja:
        # TODO
        pass

    @staticmethod
    def Transpuesta(A: MatrizCompleja) -> MatrizCompleja:
        # TODO
        pass

    @staticmethod
    def adj(A: MatrizCompleja) -> MatrizCompleja:
        # TODO
        pass

    @staticmethod
    def multMatrices(A: MatrizCompleja, B: MatrizCompleja) -> MatrizCompleja:
        # TODO
        pass

    @staticmethod
    def accion(A: MatrizCompleja, V: VectorComplejo) -> MatrizCompleja:
        # TODO
        pass

    @staticmethod
    def multMatricesR(A, B):
        C = [[0, 0], [0, 0]]
        for i in range(len(A)):
            for j in range(len(A[0])):
                for k in range(len(A[0])):
                    C[i][j] += A[i][k] * B[k][j]
        return C
