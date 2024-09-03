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
    suma = num1 + num2
    """
    (uso de funciones)
    recibe: num1 valor numerico, num2 valor numerico
    suma 2 numeros
    devuelve: variable con los numeros sumados
    """
    return suma


def resta():
    resta = num1 - num2
    """
    (uso de funciones)
    recibe: num1 valor numerico, num2 valor numerico
    resta 2 numeros
    devuelve: variable con los numeros restados
    """
    return resta

def multi():
    multi = num1 * num2
    """
    (uso de funciones)
    recibe: num1 valor numerico, num2 valor numerico
    multiplica 2 numeros
    devuelve: variable con los numeros multiplicados
    """
    return multi

def division():
    division = num1 / num2
    """
    (uso de funciones)
    recibe: num1 valor numerico, num2 valor numerico
    divide 2 numeros
    devuelve: variable con los numeros divididos
    """
    return division




"""
(uso de condicionales, funciones)
recibe: respuesta variable numerica, pregunta variable numerica o tipo cadena
funcion auxiliar para pedir numeros con los cuales navegar por medio del menu inicial.
Adicionalmente, se hace uso de las primeras funciones para poder enseñar los resultados.
devuelve: resultado de la operación matematica.
"""

if pregunta == "suma" or pregunta == "1":
    num1 = float(input("Ingresar primer numero: "))
    num2 = float(input("Ingresar segundo numero: "))
    resultado_suma = suma()
    print("La suma de los dos numeros es:", resultado_suma)

if pregunta == "resta" or pregunta == "2":
    num1 = float(input("Ingresar primer numero: "))
    num2 = float(input("Ingresar segundo numero: "))
    resultado_resta = resta()
    print("La resta de los dos numeros es: ", resultado_resta)

if pregunta == "multiplicacion" or pregunta == "4":
    num1 = float(input("Ingresar primer numero: "))
    num2 = float(input("Ingresar segundo numero: "))
    resultado_multi = multi()
    print("La resta de los dos numeros es: ", resultado_multi)

if pregunta == "division" or pregunta == "3":
    num1 = float(input("Ingresar primer numero: "))
    num2 = float(input("Ingresar segundo numero: "))
    resultado_division = division()
    print("La resta de los dos numeros es: ", resultado_division)

if pregunta == "" or pregunta >= "5":
    print("Esa funcion no existe en la calculadora")