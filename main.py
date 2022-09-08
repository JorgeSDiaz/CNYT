from Controllers.CalculadoraComplejos import CalculadoraComplejos
from Controllers.ICalculadora import ICalculadora
from Controllers.CalculadoraMatrices import CalculadoraMatrices
from Controllers.CalculadoraVectores import CalculadoraVectores


def main():
    print("Calculadora cuantica, bienvenido. Estas son las operaciones Soportadas.")
    print("1. Operaciones de numeros complejos")
    print("2. Operaciones de vectores complejos")
    print("3. Operaciones de matrices complejas")
    print("4. Salir")
    option = int(input("Elija un menú ingresando el numero\n"))
    calc: ICalculadora
    if option not in [1, 2, 3]:
        print("Por favor digite una opción válida")
        main()
    if option == 1:
        calc = CalculadoraComplejos()
    elif option == 2:
        calc = CalculadoraVectores()
    else:
        calc = CalculadoraMatrices()

    if option != 4:
        calc.printOptions()
        continua = input("Desea realizar otra operación de esta calculadora? Y/N \n") or 'Y'
        if continua.upper() == 'Y':
            calc.printOptions()
        else:
            main()


main()
