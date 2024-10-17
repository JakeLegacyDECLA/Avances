"""
Proyecto de Calculadora Cientifica Python
El programa consiste en pedir numeros al usuario para
despues hacer calculos matematicos simples e incluso complejos
en base a las mismas formulas y usos que nos permite realizar
Python, al final, el resultado es puesto en pantalla.
"""

"""
===== funcion auxiliar =====
"""

def obtener_numeros():
    """
    (uso de funciones, condicionales, ciclo)
    Función para obtener una lista de números ingresados por el usuario.
    El ingreso de números termina cuando el usuario escribe "stop".
    Devuelve: lista de números.
    """
    numeros = []
    while True:
        entrada = input("Ingrese un número"
        "(o 'stop' para terminar): ").lower()
        if entrada == "stop":
            break
        try:
            numeros.append(float(entrada))
        except ValueError:
            print("Entrada no válida,"
            "por favor ingrese un número.")
    return numeros


"""
===== funciones principales =====
"""

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


def multiplicacion(numeros):
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
            print("Error: División entre cero no permitida")
            return None
        division_total /= num
    return division_total


def tabla_multiplicar(numero):
    tabla = [[numero * i for i in range(1, 11)]]
    for i in range(1, 11):
        print(f"{numero} x {i} = {numero * i}")
    return tabla


def main():
    print("CalcuTEC")
    pregunta = input("Seleccione su operacion a hacer"
    "\n 1. Suma \n 2. Resta \n 3. Division \n "
    "4. Multiplicacion \n 5. Tablas de Multiplicar \n"
    ).lower()

    if pregunta in ["suma", "1"]:
        numeros = obtener_numeros()
        resultado_suma = suma(numeros)
        print(f"La suma de {numeros}"
        "integrados es: ", resultado_suma)

    elif pregunta in ["resta", "2"]:
        numeros = obtener_numeros()
        resultado_resta = resta(numeros)
        print(f"La resta de {numeros}"
        "integrados es: ", resultado_resta)

    elif pregunta in ["multiplicacion", "4"]:
        numeros = obtener_numeros()
        resultado_multi = multiplicacion(numeros)
        print(f"La multiplicación de {numeros}"
        "ingresados es: ", resultado_multi)

    elif pregunta in ["division", "3"]:
        numeros = obtener_numeros()
        resultado_division = division(numeros)
        print(f"La división de {numeros}" 
        "ingresados es: ", resultado_division)

    elif pregunta in ["tablas", "5"]:
        numero = int(input("Ingresa un número"
        "para mostrar su tabla de multiplicar: "))
        tabla_multiplicar(numero)

    else:
        print("Esta función no existe en la calculadora")


main()
