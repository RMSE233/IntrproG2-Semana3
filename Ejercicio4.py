# Ingresar las duraciones de los tramos del vuelo y las escalas
primer_tramo = float(input("Ingrese la duración del primer tramo del vuelo en horas: "))
primera_escala = float(input("Ingrese la duración de la primera escala en horas: "))
segundo_tramo = float(input("Ingrese la duración del segundo tramo del vuelo en horas: "))
segunda_escala = float(input("Ingrese la duración de la segunda escala en horas: "))
tercer_tramo = float(input("Ingrese la duración del tercer tramo del vuelo en horas: "))

# Sumar todas las duraciones
tiempo_total = primer_tramo + primera_escala + segundo_tramo + segunda_escala + tercer_tramo

# Mostrar el tiempo total del viaje
print("El tiempo total del viaje es:", tiempo_total, "horas.")
