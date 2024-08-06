def calcular_ventas(total_unidades, ganancia_total, precio_tableta, precio_laptop):
    for y in range(total_unidades + 1):
        x = total_unidades - y
        if precio_tableta * x + precio_laptop * y == ganancia_total:
            return x, y
    return None

total_unidades = int(input("Ingresa el total de unidades vendidas: "))
ganancia_total = int(input("Ingresa la ganancia total obtenida: "))
precio_tableta = int(input("Ingresa el precio de venta de cada tableta: "))
precio_laptop = int(input("Ingresa el precio de venta de cada laptop: "))

resultados = calcular_ventas(total_unidades, ganancia_total, precio_tableta, precio_laptop)

if resultados:
    tabletas_vendidas, laptops_vendidas = resultados
    print(f"Tabletas vendidas: {tabletas_vendidas}")
    print(f"Laptops vendidas: {laptops_vendidas}")
else:
    print("NO SE PUDO SOLUCIONAR CON LOS DATOS DADOS.")
