def historia():
    print("Tres amigos aventureros, Ana, Juan y María, llegan a Antigua Guatemala buscando una experiencia inolvidable.")
    print("Deciden explorar la ciudad y sus alrededores, pero pronto se dan cuenta de que sus elecciones los llevarán por caminos muy distintos.")

    decision_parque_central()

def decision_parque_central():
    print("\nEstán en el Parque Central.")
    print("1. Visitar las ruinas de la Catedral de Santiago.")
    print("2. Ir al mercado de artesanías.")
    choice = input("Elige una opción (1/2): ")

    if choice == "1":
        decision_ruinas()
    elif choice == "2":
        decision_mercado()
    else:
        print("Opción no válida. Intenta de nuevo.")
        decision_parque_central()

def decision_ruinas():
    print("\nHan decidido visitar las ruinas de la Catedral de Santiago.")
    print("1. Explorar los túneles subterráneos.")
    print("2. Salir y volver al Parque Central.")
    choice = input("Elige una opción (1/2): ")

    if choice == "1":
        decision_tuneles()
    elif choice == "2":
        decision_guia_turistico()
    else:
        print("Opción no válida. Intenta de nuevo.")
        decision_ruinas()

def decision_tuneles():
    print("\nEstán explorando los túneles subterráneos.")
    print("1. Seguir adelante por los túneles.")
    print("2. Salir y volver al Parque Central.")
    choice = input("Elige una opción (1/2): ")
