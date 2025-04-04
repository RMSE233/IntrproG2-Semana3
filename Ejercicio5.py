#Ingresar la cantidad total de segundos 
total_segundos = int(input("ingrese la cantidad total de segundos"))

# Calcular las horas
horas = total_segundos // 3600
resto_segundos = total_segundos % 3600

#calcular los minutos
minutos = total_segundos // 60

#calcular los segundos restantes 
segundos = resto_segundos % 60
 
 #Mostrar el tiempo en horas, minutos y segundos
print(f"El tiempo es: {horas} horas, {minutos} minutos y {segundos} segundos.")