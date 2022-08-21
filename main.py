from calculadoraCuantica import *


def printOptions():
    print("1. Suma")
    print("2. resta")
    print("3. Producto")
    print("4. división")
    print("5. modulo")
    print("6. Conjugado")
    print("7. Convertir a polares")
    print("8. Convertir a cartesianas")
    print("9. Fase")


def main():
    print("Calculadora cuantica, bienvenido.")
    printOptions()
    num = int(input("Por favor digite el numero de la operación\n"))
    c1: Complejo
    if num != 8:
        c1 = Complejo.decode(input("por favor digite el  numero de la forma a +bi\n"))
    else:
        data = input("Digite el numero de la forma rho, angulo. El angulo se lee en grados\n ").split()
        c1 = Complejo(int(data[0]), int(data[1]), isCartesiano=False)

    if num < 5:
        c2: Complejo = Complejo.decode(input("por favor digite el otro numero de la forma a +bi\n"))
        if num == 1:
            print(sumComplex(c1, c2).get())
        elif num == 2:
            print(restComplex(c1, c2).get())
        elif num == 3:
            print(multComplex(c1, c2).get())
        elif num == 4:
            print(divComplex(c1, c2).get())
        else:
            print("Operación invalida. Se reiniciará el programa.")
            main()
    elif num == 5:
        print(c1.modulo)
    elif num == 6:
        print(conjugado(c1).get())
    elif num == 7:
        print(c1.getPolar())
    elif num == 8:
        print(c1.getCartesiano())
    elif num == 9:
        print(c1.getAngle())
    else:
        print("Operación invalida. Se reiniciará el programa.")
        main()


main()
