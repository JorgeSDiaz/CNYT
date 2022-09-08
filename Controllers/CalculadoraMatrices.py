from Controllers.CalculadoraComplejos import CalculadoraComplejos
from Controllers.CalculadoraVectores import CalculadoraVectores
from Controllers.ICalculadora import ICalculadora
from Models.Complejo import Complejo
from Models.MatrizCompleja import MatrizCompleja
from Models.VectorComplejo import VectorComplejo


class CalculadoraMatrices(ICalculadora):
    def __init__(self):
        ICalculadora.__init__(self)
        self.calcVectores: CalculadoraVectores = CalculadoraVectores()

    def printOptions(self):
        print("1. Sumar")
        print("2. Inversa")
        print("3. multiplicar por escalar complejo")
        print("4. Transpuesta")
        print("5. Adjunta o daga")
        print("6. Multiplicar")
        print("7. Accion de matriz sobre vector ")
        print("8. Verificar si es unitaria ")
        print("9. Verificar si es hermitiana ")

        num = int(input("Por favor digite el numero de la operación\n"))
        texto = "Digite la matriz separando cada vector por un '|'\n"
        m1 = MatrizCompleja(MatrizCompleja.decode(input(texto)))

        if num == 1:
            m2 = MatrizCompleja(MatrizCompleja.decode(input(texto)))
            self.sumMatrices(m1, m2).get()
        elif num == 2:
            self.inversaMatriz(m1).get()
        elif num == 3:
            complejo = Complejo.recibaNum()
            self.multMatriz(m1, complejo).get()
        elif num == 4:
            self.transpuesta(m1).get()
        elif num == 5:
            self.adj(m1).get()
        elif num == 6:
            m2 = MatrizCompleja(MatrizCompleja.decode(input(texto)))
            self.multMatrices(m1, m2)
        elif num == 7:
            v = VectorComplejo.recibaNum()
            self.accion(m1, v)
        elif num == 8:
            print(self.isUnitaria(m1))
        elif num == 9:
            print(self.isHermitiana(m1))
        else:
            Exception("Not valid option")

    def sumMatrices(self, A: MatrizCompleja, B: MatrizCompleja) -> MatrizCompleja or None:
        rta = None
        if A.getDimensions() == B.getDimensions():
            lista = []
            for i in range(A.getDimensions()[1]):
                lista.append(self.calcVectores.sumVectores(A.components[i], B.components[i]))
            rta = MatrizCompleja(lista)

        return rta

    def inversaMatriz(self, A: MatrizCompleja) -> MatrizCompleja:
        num = Complejo(-1, -1)
        lista = []
        for vector in A.components:
            lista.append(self.calcVectores.multVector(vector, num))

        return MatrizCompleja(lista)

    def multMatriz(self, A: MatrizCompleja, c: Complejo) -> MatrizCompleja:
        lista = []
        for vector in A.components:
            lista.append(self.calcVectores.multVector(vector, c))

        return MatrizCompleja(lista)

    @staticmethod
    def transpuesta(A: MatrizCompleja) -> MatrizCompleja:
        listas = []
        for i in range(len(A.components)):
            lista = []
            for item in A.components:
                lista.append(item.getComplejo(i))
            listas.append(VectorComplejo(lista))

        return MatrizCompleja(listas)

    def adj(self, A: MatrizCompleja) -> MatrizCompleja:
        transpuesta = self.transpuesta(A)
        listas = []
        for vector in transpuesta.components:
            listas.append(self.calcVectores.getAdjunta(vector))

        return MatrizCompleja(listas)

    @staticmethod
    def multMatrices(A: MatrizCompleja, B: MatrizCompleja) -> MatrizCompleja or None:
        matrix = None
        if A.getDimensions()[1] == B.getDimensions()[0]:
            matrix = MatrizCompleja([VectorComplejo([Complejo(0, 0) for i in range(A.getDimensions()[0])])
                                     for j in range(B.getDimensions()[1])])
            calcComplejos = CalculadoraComplejos()

            for i in range(len(matrix)):
                for j in range(matrix.getDimensions()[1]):
                    for k in range(A.getDimensions()[0]):
                        prd = calcComplejos.multComplex(A.getPos(i, k), B.getPos(k, j))
                        value = calcComplejos.sumComplex(matrix.getPos(i, j), prd)
                        matrix.setPos(i, j, value)

        return matrix

    def accion(self, A: MatrizCompleja, V: VectorComplejo) -> MatrizCompleja:
        return self.multMatrices(A, MatrizCompleja([V]))

    @staticmethod
    def multMatricesR(A, B):
        C = [[0, 0], [0, 0]]
        for i in range(len(A)):
            for j in range(len(A[0])):
                for k in range(len(A[0])):
                    C[i][j] += A[i][k] * B[k][j]
        return C

    def isUnitaria(self, A: MatrizCompleja) -> bool:
        isUnitaria = True
        dimensiones = A.getDimensions()
        prd = self.multMatrices(A, self.adj(A))
        if prd is not None and prd.isSquare():
            for i in range(dimensiones[0]):
                for j in range(dimensiones[0]):
                    if (i == j and prd.getPos(i, i).real != 1 and prd.getPos(i, i).complejo != 0) \
                            or (i != j and prd.getPos(i, i).real != 0 and prd.getPos(i, i).complejo != 0):
                        isUnitaria = False
        else:
            isUnitaria = False
        return isUnitaria

    def isHermitiana(self, A: MatrizCompleja) -> bool:
        return A == self.adj(A)
