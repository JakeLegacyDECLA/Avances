"""
Proyecto de Calculadora Cientifica Python
El programa consiste en pedir numeros al usuario para
despues hacer calculos matematicos simples e incluso complejos
en base a las mismas formulas y usos que nos permite realizar
Python, al final, el resultado es puesto en pantalla.
"""


print("Calculadora Cientifica")
pregunta = input("Seleccione su operacion a hacer \n 1. Suma \n 2. Resta \n 3. Division \n 4. Multiplicacion \n").lower()


def suma():

    """
    (uso de funciones, condicional, ciclo)
    recibe: n, valores numericos
    suma n numeros ingresados hasta que el usuario ingrese la palabra "stop"
    devuelve: variable auxiliar con los numeros sumados
    """

    sumatotal = 0
    stop = ""

    while stop.lower() != "stop":
        stop = input("Ingrese sus numeros (PALABRA DE PARO: STOP): ")

        if stop.lower() != "stop":
            sumatotal += float(stop)

    return sumatotal


def resta():
    """
    (uso de funciones, condicionales, ciclo)
    recibe: n, valores numericos
    resta n numeros ingresados hasta que el usuario ingrese la palabra "stop"
    devuelve: variable auxiliar con los numeros restados
    """

    resta_total = None
    stop = ""

    while stop.lower() != "stop":
        stop = input("Ingrese sus numeros (PALABRA DE PARO: STOP): ")

        if stop.lower() != "stop":
            numero = float(stop)

            if resta_total is None:
                resta_total = numero 
            else:
                resta_total -= numero  

    return resta_total

def multi():
    """
    (uso de funciones, condicionales, ciclo)
    recibe: n, valores numericos
    multiplica n numeros ingresados hasta que el usuario ingrese la palabra "stop"
    devuelve: variable auxiliar con los numeros multiplicados
    """

    multi_total = None
    stop = ""

    while stop.lower() != "stop":
        stop = input("Ingrese sus numeros (PALABRA DE PARO: STOP): ")

        if stop.lower() != "stop":
            numero = float(stop)

            if multi_total is None:
                multi_total = numero
            else:
                multi_total *= numero

    return multi_total

def division():
    """
    (uso de funciones, condicionales, ciclo)
    recibe: n, valores numericos
    divide los numeros ingresados hasta que el usuario ingrese la palabra "stop"
    devuelve: variable auxiliar con los numeros divididos
    """

    division_total = None
    stop = ""

    while stop.lower() != "stop":
        stop = input("Ingrese sus numeros (PALABRA DE PARO: STOP): ")

        if stop.lower() != "stop":
            numero = float(stop)

            if division_total is None:
                division_total = numero
            else:
                if numero != 0:
                    division_total /= numero
                else:
                    return "Error: Division entre cero no permitida"

    return division_total




"""
(uso de condicionales, funciones)
recibe: respuesta variable numerica, pregunta variable numerica o tipo cadena
funcion auxiliar para pedir numeros con los cuales navegar por medio del menu inicial.
Adicionalmente, se hace uso de las primeras funciones para poder enseñar los resultados.
devuelve: resultado de la operación matematica.
"""


if pregunta == "suma" or pregunta == "1":
    resultado_suma = suma()
    print("La suma de los numeros integrados es: ", resultado_suma)

elif pregunta == "resta" or pregunta == "2":
    resultado_resta = resta()
    print("La resta de los numeros integrados es: ", resultado_resta)

elif pregunta == "multiplicacion" or pregunta == "4":
    resultado_multi = multi()
    print("La resta de los numeros ingresados es: ", resultado_multi)

elif pregunta == "division" or pregunta == "3":
    resultado_division = division()
    print("La resta de los numeros ingresados es: ", resultado_division)

elif pregunta == "" or pregunta >= "5":
    print("Esa funcion no existe en la calculadora")

        