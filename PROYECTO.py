def found_vel(distancia, tiempo):
    result = distancia / tiempo
    print("La velocidad sería", str(result), "metros por segundo")

def found_dis(velocidad, tiempo):
    result = velocidad * tiempo
    print("La distancia sería:", str(result), "metros")

def found_time(distancia, velocidad):
    result = distancia / velocidad
    print("El tiempo sería:", str(result), "segundos")

def area_cuadrado(base, altura):
    resultado = base * altura
    print("El área del cuadrado sería:", str(resultado), "metros cuadrados")

def area_triangulo(base, altura):
    resultado = base * altura / 2
    print("El área del triángulo sería:", str(resultado), "metros cuadrados")

def perimetro(lado1, lado2, lado3, lado4):
    resultado = lado1 + lado2 + lado3 + lado4
    print("El perímetro de su figura sería:", str(resultado), "metros")

def masa_molar(atomo1, atomo2, elemento1, elemento2):
    resultado = atomo1 * atomo2 + elemento1 * elemento2
    print("La masa molar sería:", str(resultado), "")

def fisica():
    Fisica = input("""Qué variable quiere encontrar?
             1. Velocidad
             2. Distancia
             3. Tiempo
             Qué variable quiere encontrar?: """)
    
    if Fisica == "1":
        time = float(input("Ingrese el tiempo en segundos: "))
        distance = float(input("Ingrese su distancia en metros: "))
        found_vel(distance, time)

    if Fisica == "2":
        speed = float(input("Ingrese su velocidad en metros por segundo: "))
        time = float(input("Ingrese su tiempo en segundos: "))
        found_dis(speed, time)

    if Fisica == "3":
        distance = float(input("Ingrese su distancia en metros: "))
        speed = float(input("Ingrese su velocidad en metros por segundo: "))
        found_time(distance, speed)

def mate():
    math = input("""Qué operación matemática quiere realizar
            1. Área de un Cuadrado
            2. Área de un Triángulo
            3. Perímetro de una figura de 4 lados
            : """)
    if math == "1":
        base = float(input("Ingrese la base de su figura en metros: "))
        altura = float(input("Ingrese su altura en metros: "))
        area_cuadrado(base, altura)
    
    if math == "2":
        base = float(input("Ingrese su base en metros: "))
        altura = float(input("Ingrese su altura en metros: "))
        area_triangulo(base, altura)

    if math == "3":
        lado1 = float(input("Ingrese la medida del lado 1: "))
        lado2 = float(input("Ingrese la medida del lado 2: "))
        lado3 = float(input("Ingrese la medida del lado 3: "))
        lado4 = float(input("Ingrese la medida del lado 4: "))
        perimetro(lado1, lado2, lado3, lado4)

def quimica():
    quimica = input("""Qué operación desea realizar
                  1. Calcular la Masa Molar
                  2. Conversión de moles a Gramos
                  3. Concentración Molar en una solución
                  4. Balance de Ecuación
                                        : """)
    if quimica == "1":
        atomo1 = float(input("Ingrese el número de átomos de su primer elemento: "))
        atomo2 = float(input("Ingrese el número de átomos de su segundo elemento: "))
        elemento1 = float(input("Ingrese el número de átomos del siguiente elemento: "))
        elemento2 = float(input("Ingrese el número de átomos del segundo elemento: "))
        masa_molar(atomo1, atomo2, elemento1, elemento2)

# Inicio del programa
inicio = input("""Sobre qué materia quiere resolver su problema?
      1. Física
      2. Matemáticas
      3. Química
      : """)

if inicio == "1":
    fisica()

elif inicio == "2":
    mate()
    
elif inicio == "3":
    quimica()
