# Ejemplo con datos totalmente distintos (Temperatura):
def calcular_grados(celsius):
    fahrenheit = (celsius * 1.8) + 32
    return fahrenheit

def mostrar_clima(grados_f):
    print(f"🌡️ La temperatura actual es de {grados_f} °F.")

# Guardas el retorno y lo envías a la siguiente
temperatura_actual = calcular_grados(25)
mostrar_clima(temperatura_actual)
# 1. Función que calcula y retorna el poder total
def calcular_fuerza(nivel, espada):
    fuerza_total = nivel * espada
    return fuerza_total

# 2. Función que recibe la fuerza y muestra el ataque
def simular_ataque(fuerza, enemigo):
    print(f"⚔️ ¡Atacaste al {enemigo} con {fuerza} puntos de poder!")

# 3. Código principal (fuera de las funciones)
poder_jugador = calcular_fuerza(5, 10)
simular_ataque(poder_jugador, "Zombie 🧟")