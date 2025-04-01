temp_fah = float (input("ingresa la temperatura en F: "))
temp_cel = temp_fah - 32
temp_cel = temp_cel * 5
temp_cel = temp_cel / 9

temp_cel = ((temp_fah - 32) * 5/9)


temp_kel = temp_cel + 273.15
print(f"Grados celsius {temp_cel:.2f}")
print(f"Grados kelvin, {temp_kel:.2f}")