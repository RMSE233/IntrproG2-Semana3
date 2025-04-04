# Ingresar datos
duracion_pelicula = float(input("Ingrese la duración de la película en minutos: "))
comerciales_previos = float(input("Ingrese la duración de los comerciales previos en minutos: "))
cantidad_pausas = int(input("Ingrese la cantidad de pausas comerciales durante la película: "))
duracion_pausa = float(input("Ingrese la duración de cada pausa comercial en minutos: "))

# Calcular el total de comerciales
total_comerciales = cantidad_pausas * duracion_pausa

# Calcular tiempo total de la película
tiempo_total = duracion_pelicula + comerciales_previos + total_comerciales

# Mostrar el resultado
print(f"El tiempo total de la película con comerciales es: {tiempo_total} minutos.")