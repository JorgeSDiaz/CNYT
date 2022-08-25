from Controllers.CalculadoraComplejos import CalculadoraComplejos
from Models.Complejo import Complejo


def test():
    c = CalculadoraComplejos()
    c1 = Complejo(5, -10)
    c2 = Complejo(-2, 13)
    rta = c.sumComplex(c1, c2)
    assert(rta.real == 3)
    assert(rta.complejo == 3)
    rta = c.restComplex(c1, c2)
    assert(rta.real == 7)
    assert(rta.complejo == -23)
    rta = c.multComplex(c1, c2)
    assert(rta.real == 120)
    assert(rta.complejo == 85)
    c1 = Complejo(-2, 1)
    c2 = Complejo(1, 2)
    rta = c.divComplex(c1, c2)
    assert(rta.real == 0)
    assert(rta.complejo == 1)
    assert(c1.modulo == 5**0.5)
    assert(c2.modulo == 5**0.5)
    assert(rta.modulo == 1.0)
    rta = c.conjugado(c1)
    assert(rta.complejo == -1)
    assert(c.getFase(c2) > 62 and c.getFase(c2) < 65)
