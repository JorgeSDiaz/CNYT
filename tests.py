from calculadoraCuantica import *

def test():
    c1 = Complejo(5, -10)
    c2 = Complejo(-2, 13)
    rta = sumComplex(c1, c2)
    assert(rta.real == 3)
    assert(rta.complejo == 3)
    rta = restComplex(c1, c2)
    assert(rta.real == 7)
    assert(rta.complejo == -23)
    rta = multComplex(c1, c2)
    assert(rta.real == 120)
    assert(rta.complejo == 85)
    c1 = Complejo(-2, 1)
    c2 = Complejo(1, 2)
    rta = divComplex(c1, c2)
    assert(rta.real == 0)
    assert(rta.complejo == 1)
    assert(c1.modulo == 5**0.5)
    assert(c2.modulo == 5**0.5)
    assert(rta.modulo == 1.0)
    rta = conjugado(c1)
    assert(rta.complejo == -1)
    assert(getFase(c2) > 62 and getFase(c2) < 65)


test()
