# Boss Battle Mundo 4 - Sistema de Seguridad y Acceso a la Fortaleza
# Jugadora: Itza

nivel = int(input("Ingresa tu nivel: "))
llave = input("¿Tienes la llave del portal? (si/no): ").lower()
ronda = int(input("Ingresa la ronda actual: "))

# Evaluación de Acceso
if nivel >= 20 or llave == "si":
    print(f"\n¡Acceso Total (VIP) concedido a Nivel {nivel}! Bienvenido a la fortaleza.")
elif nivel >= 10 and ronda < 5:
    print(f"\nAcceso Condicional concedido (Nivel {nivel}, Ronda {ronda}). ¡Avanza con precaución!")
else:
    print(f"\nAcceso Denegado. Nivel {nivel} insuficiente o la ronda {ronda} es muy avanzada.")