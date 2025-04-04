# Ingresar precio original y descuento
precio = float(input("Ingrese el precio original del producto: "))
descuento = float(input("Ingrese el porcentaje de descuento: "))

# Calcular el precio con descuento
descuento_monto = (precio * descuento) / 100
precio_con_descuento = precio - descuento_monto

# Ingresar porcentaje de IVA
iva = float(input("Ingrese el porcentaje de IVA: "))

# Calcular el IVA y precio final
iva_monto = (precio_con_descuento * iva) / 100
precio_final = precio_con_descuento + iva_monto

# Mostrar los resultados
print("Precio original:", precio)
print("Precio con descuento:", precio_con_descuento)
print("IVA calculado:", iva_monto)
print("Precio final:", precio_final)