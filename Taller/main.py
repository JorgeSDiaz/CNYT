class Nodo:

    def __init__(self, personas, name, nodos=None):
        if nodos is None:
            nodos = []
        self.personas = personas
        self.nodos = nodos
        self.name = name

    def ingrese(self, persona):
        self.personas += persona

    def saque(self, personas=1):
        #Por cada nodo
        #si aun tengo personas y si personas > 0
        if self.personas >= personas:
            for nodo in self.nodos:
                nodo.ingrese(1)
                personas -= 1
                self.personas -= 1

    def status(self):
        print("{0} {1}".format(self.name, self.personas))


def execClick(nodos: list[Nodo], number):
    print("click {0}".format(number))
    print(len(nodos))
    for nodo in nodos:
        nodo.saque()

    for nodo in nodos:
        nodo.status()


def main():
    n0 = Nodo(1, "0")
    n1 = Nodo(1, "1")
    n2 = Nodo(1, "2")
    n3 = Nodo(1, "3")
    n4 = Nodo(1, "4")
    n5 = Nodo(1, "5")
    n6 = Nodo(1, "6")
    n7 = Nodo(1, "7")
    n8 = Nodo(1, "8")
    n0.nodos = [n1]
    n1.nodos = [n0]
    n2.nodos = [n5]
    n3.nodos = [n3]
    n4.nodos = [n7]
    n5.nodos = [n8]
    n6.nodos = [n7]
    n7.nodos = [n8]
    n8.nodos = [n8]
    nodos = [n0, n1, n2, n3, n4, n5, n6, n7, n8]
    execClick(nodos, 1)
    execClick(nodos, 2)


main()
