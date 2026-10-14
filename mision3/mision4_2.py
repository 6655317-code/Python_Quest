# Misión 4.2 - Rutas Múltiples con elif
vida = int(input("Ingresa tu vida actual (0 a 20): "))

if vida >= 15:
    print(f"Vida: {vida}. ¡Estás listo para la batalla!")
elif vida >= 5:
    print(f"Vida: {vida}. Cuidado, necesitas comer algo.")
else:
    print(f"Vida: {vida}. ¡Peligro crítico! Busca refugio ya.")