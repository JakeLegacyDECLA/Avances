"""
Proyecto de Calculadora Cientifica Python
El programa consiste en pedir numeros al usuario para
despues hacer calculos matematicos simples e incluso complejos
en base a las mismas formulas y usos que nos permite realizar
Python, al final, el resultado es puesto en pantalla.
"""
import numpy as np

print("Calculadora Cientifica")
pregunta = input("Seleccione su operacion a hacer \n 1. Suma \n 2. Resta \n 3. Division \n 4. Multiplicacion \n 5. Tablas de Multiplicar \n").lower()
pregunta = pregunta.lower()

def obtener_numeros():
    """
    (uso de funciones, condicionales, ciclo)
    Función para obtener una lista de números ingresados por el usuario.
    El ingreso de números termina cuando el usuario escribe "stop".
    Devuelve: lista de números.
    """
    numeros = []
    while True:
        entrada = input("Ingrese un número (o 'stop' para terminar): ").lower()
        if entrada == "stop":
            break
        try:
            numeros.append(float(entrada))
        except ValueError:
            print("Entrada no válida, por favor ingrese un número.")
    return numeros

def suma(numeros):

    """
    (uso de funciones, ciclo)
    recibe: lista
    suma n numeros ingresados en la lista
    devuelve: lista sumada, variable auxiliar
    """

    return sum(numeros)


def resta(numeros):
    """
    (uso de funciones, ciclo)
    recibe: lista
    resta n numeros ingresados ingresados en la lista
    devuelve: lista restada, variable auxiliar
    """

    resta_total = numeros[0]
    for num in numeros[1:]:
        resta_total -= num

    return resta_total

def multi(numeros):
    """
    (uso de funciones, ciclo)
    recibe: lista
    multiplica n numeros ingresados en la lista
    devuelve: lista multiplicada, variable auxiliar
    """

    multi_total = 1
    for num in numeros:
     multi_total *= num

    return multi_total


def division(numeros):
    """
    (uso de funciones, ciclo)
    recibe: lista
    divide n numeros ingresados en la lista
    devuelve: lista dividida, variable auxiliar
    """

    division_total = numeros[0]

    for num in numeros[1:]:
        if num == 0:
            return print("Error: División entre cero no permitida")
        division_total /= num

    return division_total

def tabla_multiplicar(numero):
    """
    (uso de funciones, listas)
    recibe: listas
    se crea una lista anidada que contiene
    los numeros del 1 al 10, para despues
    multiplicar el numero dado por el usuario
    con los de la lista
    devuelve: la tabla del 1 al 10 del numero otorgado
    """
    tabla = [[numero * i for i in range(1, 11)]]
    
    for i in range(1, 11):
        print(f"{numero} x {i} = {numero * i}")

    return tabla



"""
(uso de condicionales, funciones)
recibe: respuesta variable numerica, pregunta variable numerica o tipo cadena
funcion auxiliar para pedir numeros con los cuales navegar por medio del menu inicial.
Adicionalmente, se hace uso de las primeras funciones para poder enseñar los resultados.
devuelve: resultado de la operación matematica.
"""


if pregunta == "suma" or pregunta == "1":
    numeros = obtener_numeros()
    resultado_suma = suma(numeros)
    print(f"La suma de {numeros} integrados es: ", resultado_suma)

elif pregunta == "resta" or pregunta == "2":
    numeros = obtener_numeros()
    resultado_resta = resta(numeros)
    print(f"La resta de {numeros} integrados es: ", resultado_resta)

elif pregunta == "multiplicacion" or pregunta == "4":
    numeros = obtener_numeros()
    resultado_multi = multi(numeros)
    print(f"La resta de {numeros} ingresados es: ", resultado_multi)

elif pregunta == "division" or pregunta == "3":
    numeros = obtener_numeros()
    resultado_division = division(numeros)
    print(f"La resta de {numeros} ingresados es: ", resultado_division)

elif pregunta == "tablas" or pregunta == "5":
    numero = int(input("Ingresa un número para mostrar su tabla de multiplicar: "))
    tabla_multiplicar(numero)

elif pregunta == "" or pregunta >= "6":
    print("Esa funcion no existe en la calculadora")

        
