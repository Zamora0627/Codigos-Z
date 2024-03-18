def main():
    print("Bienvenido al Programa de Monitoreo de Especies en un Ecosistema.")
    print("Este programa te permitirá ingresar los avistamientos de diferentes especies en un ecosistema y generar informes sobre su distribución.")
    print("Por favor, ingresa el nombre de las especies avistadas. Cuando hayas terminado, escribe 'fin' para generar los informes.")

    avistamientos = {}

    while True:
        especie = input("Ingrese el nombre de la especie avistada (o 'fin' para terminar): ").strip().capitalize()
        
        if especie == 'Fin':
            break
        
        if especie in avistamientos:
            avistamientos[especie] += 1
        else:
            avistamientos[especie] = 1

    print("\nGenerando informes...")
    print("Distribución de especies avistadas:")
    for especie, cantidad in avistamientos.items():
        print(f"{especie}: {cantidad} avistamientos")

    especie_mas_comun = max(avistamientos, key=avistamientos.get)
    cantidad_mas_comun = avistamientos[especie_mas_comun]
    print(f"\nLa especie más común es '{especie_mas_comun}' con {cantidad_mas_comun} avistamientos.")

    print("\n¡Gracias por utilizar el Programa de Monitoreo de Especies en un Ecosistema!")

if __name__ == "__main__":
    main()
