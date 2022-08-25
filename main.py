from Controllers.CalculadoraComplejos import CalculadoraComplejos
from Controllers.ICalculadora import ICalculadora
from Controllers.CalculadoraMatrices import CalculadoraMatrices
from Controllers.CalculadoraVectores import CalculadoraVectores


def main():
    print("Calculadora cuantica, bienvenido. Estas son las operaciones Soportadas.")
    print("1. Operaciones de numeros complejos")
    print("2. Operaciones de vectores complejos")
    print("3. Operaciones de matrices complejas")
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
    calc.printOptions()
    continua = input("Desea realizar otra operación? Se usarán los mismos valores.Y/N \n") or 'Y'
    if continua.upper() == 'Y':
        calc.printOptions()
    # TODO pasar calculadoras a los controllers


main()
