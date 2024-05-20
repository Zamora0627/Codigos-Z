def segundos_a_minutos(segundos):
    return segundos / 60

def minutos_a_horas(minutos):
    return minutos / 60

def horas_a_segundos(horas):
    return horas / 3600



print("Inicio de Programa")

segundos=float(input("Ingrese un valor en segundos"))

print(segundos_a_minutos(segundos))

minutos=float(input("Ingrese un valor en minutos"))

print(minutos_a_horas(minutos))

horas=float(input("Ingrese un valor en horas"))

print(horas_a_segundos(segundos))
