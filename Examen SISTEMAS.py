def calcular_tarifa_viaje(distancia_km, tiempo_min, hora):
    tarifa_base = 5.00
    tarifa_por_km = 2.50
    tarifa_por_minuto = 0.50
    
    tarifa_total = tarifa_base + (distancia_km * tarifa_por_km) + (tiempo_min * tarifa_por_minuto)
  
    hora_pico = if (hora >= 7 and hora < 9) or (hora >= 17 and hora < 19)
    
    if hora_pico:
        recargo = tarifa_total * 0.20
        tarifa_total += recargo
    
    return tarifa_total

distancia = float(input("Ingrese la distancia recorrida en kilómetros: "))
tiempo = float(input("Ingrese el tiempo de viaje en minutos: "))
hora_inicio = int(input("Ingrese la hora de inicio del viaje (formato de 24 horas): "))

tarifa_total = calcular_tarifa_viaje(distancia, tiempo, hora_inicio)
print("La tarifa total del viaje es: Q{}(tarifa_total))


