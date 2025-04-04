# Ingresar peso y altura
peso = float(input("Ingrese su peso en kilogramos: "))
altura = float(input("Ingrese su altura en metros: "))

# Calcular IMC
altura_cuadrada = altura * altura
IMC = peso / altura_cuadrada

# Redondear IMC a 2 decimales
IMC_redondeado = round(IMC, 2)

# Mostrar el resultado y clasificación
print("Su IMC es:", IMC_redondeado)

if IMC_redondeado < 18.5:
    print("Clasificación: Bajo peso")
elif IMC_redondeado < 24.9:
    print("Clasificación: Peso normal")
elif IMC_redondeado < 29.9:
    print("Clasificación: Sobrepeso")
else:
    print("Clasificación: Obesidad")