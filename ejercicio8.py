# Ingresar cantidad en dólares
dolares = float(input("Ingrese la cantidad en dólares: "))

# Tasas de cambio
tasa_euros = 0.92
tasa_libras = 0.75
tasa_yenes = 134.21

# Convertir a otras monedas
euros = dolares * tasa_euros
libras = dolares * tasa_libras
yenes = dolares * tasa_yenes

# Mostrar resultados
print(f"{dolares} dólares equivalen a {euros} euros, {libras} libras y {yenes} yenes.")