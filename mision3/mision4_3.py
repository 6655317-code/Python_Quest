# Misión 4.3 - Operadores Lógicos (and, or, not)
diamantes = int(input("¿Cuántos diamantes tienes?: "))
palos = int(input("¿Cuántos palos de madera tienes?: "))

if diamantes >= 2 and palos >= 1:
    print(f"¡Tienes {diamantes} diamantes y {palos} palos! Puedes fabricar una Espada de Diamante ⚔️.")
else:
    print("Materiales insuficientes para fabricar la espada.")