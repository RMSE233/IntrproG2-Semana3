# Ingresar el salario bruto del empleado
salario_bruto = float(input("Ingrese el salario bruto del empleado: "))

# Calcular los descuentos
impuesto_renta = salario_bruto * 0.10  # 10% impuesto sobre la renta
seguro_social = salario_bruto * 0.05  # 5% seguro social
fondo_pensiones = salario_bruto * 0.03  # 3% fondo de pensiones

# Calcular el total de los descuentos
descuentos_totales = impuesto_renta + seguro_social + fondo_pensiones

# Calcular el salario neto
salario_neto = salario_bruto - descuentos_totales

# Mostrar resultados
print("El salario bruto es:", salario_bruto)
print("Los descuentos totales son:", descuentos_totales)
print("El salario neto es:", salario_neto)