from Controllers.CalculadoraMatrices import CalculadoraMatrices
from Models.Complejo import Complejo
from Models.MatrizCompleja import MatrizCompleja
from Models.VectorComplejo import VectorComplejo


def test():
    A = MatrizCompleja(MatrizCompleja.decode("1 -2i, 2 +1i | 2 -1i, 1 +2i"))
    hadamard = MatrizCompleja([VectorComplejo([Complejo(1, 0), Complejo(1, 0)]),
                               VectorComplejo([Complejo(1, 0), Complejo(-1, 0)])])
    c = CalculadoraMatrices()
    assert(c.adj(A) == MatrizCompleja([VectorComplejo([Complejo(1, 2), Complejo(2, 1)]),
                                       VectorComplejo([Complejo(2, -1), Complejo(1, -2)])]))
    assert(c.adj(hadamard) == hadamard)
    assert(MatrizCompleja([VectorComplejo([Complejo(3, -3), Complejo(3, 3)]),
                           VectorComplejo([Complejo(-1, -1), Complejo(1, -1)])])
           == c.multMatrices(A, hadamard))
    assert(c.accion(A, VectorComplejo([Complejo(1, 1), Complejo(-1, 0)])) ==
           MatrizCompleja([VectorComplejo([Complejo(1, 0), Complejo(0, 1)])]))
    assert(c.isUnitaria(hadamard))
    assert(c.isHermitiana(hadamard))
