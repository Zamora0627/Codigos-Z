proyecto

import math

# Funciones de física
def calculate_velocity(distance, time):
    """Calcula la velocidad dada la distancia y el tiempo."""
    velocity = distance / time
    return velocity

def calculate_force(mass, acceleration):
    """Calcula la fuerza dada la masa y la aceleración."""
    force = mass * acceleration
    return force

def calculate_torque(force, distance):
    """Calcula el torque dada la fuerza y la distancia."""
    torque = force * distance
    return torque

# Funciones de matemáticas
def calculate_quadratic_formula(a, b, c):
    """Calcula las soluciones de una ecuación cuadrática."""
    discriminant = b**2 - 4*a*c
    if discriminant < 0:
        return None  # Soluciones imaginarias
    elif discriminant == 0:
        x = -b / (2*a)
        return x, x  # Solución repetida
    else:
        x1 = (-b + math.sqrt(discriminant)) / (2*a)
        x2 = (-b - math.sqrt(discriminant)) / (2*a)
        return x1, x2

def calculate_binomial_coefficient(n, k):
    """Calcula el coeficiente binomial (n choose k)."""
    if k < 0 or k > n:
        return 0
    else:
        return math.factorial(n) // (math.factorial(k) * math.factorial(n - k))

def calculate_cube_volume(side_length):
    """Calcula el volumen de un cubo dado el lado."""
    volume = side_length ** 3
    return volume

# Agrega más funciones según sea necesario...

# Ejemplos de uso
if __name__ == "__main__":
    # Ejemplo de física
    distance = 10  # metros
    time = 2  # segundos
    velocity = calculate_velocity(distance, time)
    print("Velocidad:", velocity, "m/s")

    # Ejemplo de matemáticas
    a = 1
    b = -3
    c = 2
    solutions = calculate_quadratic_formula(a, b, c)
    print("Soluciones de la ecuación cuadrática:", solutions)
