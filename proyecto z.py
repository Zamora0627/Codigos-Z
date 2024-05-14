def calcular_velocidad(distancia, tiempo):
    """
    Calcula la velocidad a partir de la distancia y el tiempo.

    Args:
        distancia (float): La distancia recorrida en metros.
        tiempo (float): El tiempo transcurrido en segundos.

    Returns:
        float: La velocidad en metros por segundo.
    """
    velocidad = distancia / tiempo
    print(f"La velocidad es de {velocidad:.2f} metros por segundo.")
    return velocidad

def calcular_distancia(velocidad, tiempo):
    """
    Calcula la distancia recorrida a partir de la velocidad y el tiempo.

    Args:
        velocidad (float): La velocidad en metros por segundo.
        tiempo (float): El tiempo transcurrido en segundos.

    Returns:
        float: La distancia recorrida en metros.
    """
    distancia = velocidad * tiempo
    print(f"La distancia recorrida es de {distancia:.2f} metros.")
    return distancia

def calcular_tiempo(distancia, velocidad):
    """
    Calcula el tiempo transcurrido a partir de la distancia y la velocidad.

    Args:
        distancia (float): La distancia recorrida en metros.
        velocidad (float): La velocidad en metros por segundo.

    Returns:
        float: El tiempo transcurrido en segundos.
    """
    tiempo = distancia / velocidad
    print(f"El tiempo transcurrido es de {tiempo:.2f} segundos.")
    return tiempo

def fisica():
    """
    Módulo para realizar cálculos de física.

    Ofrece funciones para calcular la velocidad, la distancia y el tiempo a partir de dos de estas magnitudes.
    """
    while True:
        print("\nMenú de física:")
        print("1. Calcular velocidad")
        print("2. Calcular distancia")
        print("3. Calcular tiempo")
        print("4. Salir")

        opcion = input("Ingrese la opción deseada (1-4): ")

        if opcion == "1":
            distancia = float(input("Ingrese la distancia recorrida en metros: "))
            tiempo = float(input("Ingrese el tiempo transcurrido en segundos: "))
            calcular_velocidad(distancia, tiempo)

        elif opcion == "2":
            velocidad = float(input("Ingrese la velocidad en metros por segundo: "))
            tiempo = float(input("Ingrese el tiempo transcurrido en segundos: "))
            calcular_distancia(velocidad, tiempo)

        elif opcion == "3":
            distancia = float(input("Ingrese la distancia recorrida en metros: "))
            velocidad = float(input("Ingrese la velocidad en metros por segundo: "))
            calcular_tiempo(distancia, velocidad)

        elif opcion == "4":
            print("Saliendo del menú de física.")
            break

        else:
            print("Opción no válida. Intente nuevamente.")

def calcular_area_cuadrado(base, altura):
    """
    Calcula el área de un cuadrado a partir de su base y altura.

    Args:
        base (float): La longitud de la base del cuadrado en metros.
        altura (float): La longitud de la altura del cuadrado en metros.

    Returns:
        float: El área del cuadrado en metros cuadrados.
    """
    area = base * altura
    print(f"El área del cuadrado es de {area:.2f} metros cuadrados.")
    return area

def calcular_area_triangulo

