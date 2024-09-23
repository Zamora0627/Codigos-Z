def celsius_to_fahrenheit(celsius):
    return (celsius * 9/5) + 32

def fahrenheit_to_celsius(fahrenheit):
    return (fahrenheit - 32) * 5/9

def mostrar_menu():
    print("\nConversor de Temperatura")
    print("1. Convertir de Celsius a Fahrenheit")
    print("2. Convertir de Fahrenheit a Celsius")
    print("3. Salir")

def validar_rango(temperatura, tipo_conversion):
    if tipo_conversion == 1:  # Celsius a Fahrenheit
        if -273.15 <= temperatura <= 1000:  # Rango de temperatura en Celsius
            return True
    elif tipo_conversion == 2:  # Fahrenheit a Celsius
        if -459.67 <= temperatura <= 1832:  # Rango de temperatura en Fahrenheit
            return True
    return False

def main():
    while True:
        mostrar_menu()
        opcion = input("Elija una opción: ")

        if opcion == '1':
            try:
                celsius = float(input("Ingrese la temperatura en Celsius: "))
                if validar_rango(celsius, 1):
                    fahrenheit = celsius_to_fahrenheit(celsius)
                    print(f"{celsius}°C es igual a {fahrenheit:.2f}°F")
                else:
                    print("Temperatura fuera de rango. El rango válido para Celsius es de -273.15 a 1000.")
            except ValueError:
                print("Por favor, ingrese un número válido.")
        
        elif opcion == '2':
            try:
                fahrenheit = float(input("Ingrese la temperatura en Fahrenheit: "))
                if validar_rango(fahrenheit, 2):
                    celsius = fahrenheit_to_celsius(fahrenheit)
                    print(f"{fahrenheit}°F es igual a {celsius:.2f}°C")
                else:
                    print("Temperatura fuera de rango. El rango válido para Fahrenheit es de -459.67 a 1832.")
            except ValueError:
                print("Por favor, ingrese un número válido.")

        elif opcion == '3':
            print("Saliendo del programa...")
            break

        else:
            print("Opción no válida. Intente nuevamente.")

if __name__ == "__main__":
    main()
