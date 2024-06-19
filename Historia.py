def inicio():
    print("Bienvenido a la historia interactiva.")
    decision1()

def decision1():
    print("\nDecisión 1: ¿El personaje va a la ciudad o al bosque?")
    print("1. Ciudad")
    print("2. Bosque")
    choice = input("Elige 1 o 2: ")
    if choice == "1":
        ciudad()
    elif choice == "2":
        bosque()
    else:
        print("Opción inválida. Intenta de nuevo.")
        decision1()

def ciudad():
    print("\nHas elegido ir a la ciudad.")
    print("Decisión 2A: ¿Habla con el anciano o ignora al anciano?")
    print("1. Habla con el anciano")
    print("2. Ignora al anciano")
    choice = input("Elige 1 o 2: ")
    if choice == "1":
        final1()
    elif choice == "2":
        decision3A()
    else:
        print("Opción inválida. Intenta de nuevo.")
        ciudad()

def decision3A():
    print("\nHas decidido ignorar al anciano.")
    print("Decisión 3A: ¿Ayuda al anciano o sigue su camino?")
    print("1. Ayuda al anciano")
    print("2. Sigue su camino")
    choice = input("Elige 1 o 2: ")
    if choice == "1":
        decision4A()
    elif choice == "2":
        decision4B()
    else:
        print("Opción inválida. Intenta de nuevo.")
        decision3A()

def decision4A():
    print("\nHas decidido ayudar al anciano.")
    print("Decisión 4A: ¿Acepta la misión del anciano o la rechaza?")
    print("1. Acepta la misión")
    print("2. Rechaza la misión")
    choice = input("Elige 1 o 2: ")
    if choice == "1":
        final2()
    elif choice == "2":
        decision5A()
    else:
        print("Opción inválida. Intenta de nuevo.")
        decision4A()

def decision4B():
    print("\nHas decidido seguir tu camino.")
    print("Decisión 4B: ¿Entra a la taberna o sigue caminando?")
    print("1. Entra a la taberna")
    print("2. Sigue caminando")
    choice = input("Elige 1 o 2: ")
    if choice == "1":
        final3()
    elif choice == "2":
        decision5B()
    else:
        print("Opción inválida. Intenta de nuevo.")
        decision4B()

def decision5A():
    print("\nHas decidido rechazar la misión del anciano.")
    print("Decisión 5A: ¿Regresa con el anciano o sigue su camino?")
    print("1. Regresa con el anciano")
    print("2. Sigue su camino")
    choice = input("Elige 1 o 2: ")
    if choice == "1":
        final3()
    elif choice == "2":
        final2()
    else:
        print("Opción inválida. Intenta de nuevo.")
        decision5A()

def decision5B():
    print("\nHas decidido seguir caminando.")
    print("Decisión 5B: ¿Visita el mercado o sigue caminando?")
    print("1. Visita el mercado")
    print("2. Sigue caminando")
    choice = input("Elige 1 o 2: ")
    if choice == "1":
        final1()
    elif choice == "2":
        final3()
    else:
        print("Opción inválida. Intenta de nuevo.")
        decision5B()

def bosque():
    print("\nHas elegido ir al bosque.")
    print("Decisión 2B: ¿Explora la cueva o sigue el sendero?")
    print("1. Explora la cueva")
    print("2. Sigue el sendero")
    choice = input("Elige 1 o 2: ")
    if choice == "1":
        decision3B()
    elif choice == "2":
        final3()
    else:
        print("Opción inválida. Intenta de nuevo.")
        bosque()

def decision3B():
    print("\nHas decidido explorar la cueva.")
    print("Decisión 3B: ¿Lucha contra el monstruo o huye?")
    print("1. Lucha contra el monstruo")
    print("2. Huye")
    choice = input("Elige 1 o 2: ")
    if choice == "1":
        decision4C()
    elif choice == "2":
        decision4D()
    else:
        print("Opción inválida. Intenta de nuevo.")
        decision3B()

def decision4C():
    print("\nHas decidido luchar contra el monstruo.")
    print("Decisión 4C: ¿Usa magia o espada?")
    print("1. Usa magia")
    print("2. Usa espada")
    choice = input("Elige 1 o 2: ")
    if choice == "1":
        final1()
    elif choice == "2":
        final2()
    else:
        print("Opción inválida. Intenta de nuevo.")
        decision4C()

def decision4D():
    print("\nHas decidido huir.")
    print("Decisión 4D: ¿Busca ayuda o se esconde?")
    print("1. Busca ayuda")
    print("2. Se esconde")
    choice = input("Elige 1 o 2: ")
    if choice == "1":
        final3()
    elif choice == "2":
        decision5C()
    else:
        print("Opción inválida. Intenta de nuevo.")
        decision4D()

def decision5C():
    print("\nHas decidido esconderte.")
    print("Decisión 5C: ¿Regresa a la cueva o sigue corriendo
