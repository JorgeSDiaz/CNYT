from Models.VectorComplejo import VectorComplejo
from Models.Complejo import Complejo
from Controllers.CalculadoraVectores import CalculadoraVectores


def test():
    v = VectorComplejo(VectorComplejo.decode("3 +4i, -1 -2i"))
    c = CalculadoraVectores()
    v2 = c.multVector(v, Complejo(2, 0))
    assert(v2.getComplejo(0) == Complejo(6, 8) and v2.getComplejo(1) == Complejo(-2, -4))
    assert(c.sumVectores(v, v2) == VectorComplejo([Complejo(9, 12), Complejo(-3, -6)]))
    assert(c.norma(v) == 30**(1/2))
    assert(c.inversoVector(v) == VectorComplejo([Complejo(-3, -4), Complejo(1, 2)]))
    assert(c.productoInterno(v, v) == 30)
    assert(c.getAdjunta(v) == VectorComplejo([Complejo(3, -4), Complejo(-1, 2)]))

