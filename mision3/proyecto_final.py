class Robot:
    def __init__(self, modelo, energia):
        self.modelo = modelo
        self.energia = energia

    def disparar(self, objetivo):
        objetivo.energia -= 20
        print(f"💥 {self.modelo} disparó a {objetivo.modelo}.")

r1 = Robot("Alpha", 100)
r2 = Robot("Beta", 50)

while r2.energia > 0:
    r1.disparar(r2)
    print(f"Energía de Beta: {r2.energia}")
    def guardar_partida(self):
    with open("partida_final.txt", "w") as archivo:
        archivo.write(f"{self.nombre}\n{self.salud}\n{self.fuerza}\n")
    print("💾 Partida guardada exitosamente.")

def cargar_partida(self):
    try:
        with open("partida_final.txt", "r") as archivo:
            lineas = archivo.readlines()
            self.nombre = lineas[0].strip()
            self.salud = int(lineas[1].strip())
            self.fuerza = int(lineas[2].strip())
        print("📜 Partida cargada exitosamente.")
    except FileNotFoundError:
        print("⚠️ No hay partida guardada previa.")
        # Misión 10.3 - Persistencia de Estado (Guardar y Cargar Partida)
# Jugadora: Itza

class Jugador:
    def __init__(self, nombre):
        self.nombre = nombre
        self.salud = 100
        self.fuerza = 25
        self.inventario = ["Espada de Hierro ⚔️", "Poción de Vida 🧪"]

    def mostrar_estado(self):
        print(f"🛡️ JUGADOR: {self.nombre}")
        print(f"❤️ Salud: {self.salud}")
        print(f"⚔️ Fuerza: {self.fuerza}")
        print(f"🎒 Inventario: {', '.join(self.inventario)}")

    def guardar_partida(self):
        with open("partida_final.txt", "w") as archivo:
    
        print("💾 Partida guardada exitosamente.")

    def cargar_partida(self):
        try:
            with open("partida_final.txt", "r") as archivo:
                lineas = archivo.readlines()
                self.nombre = lineas[0].strip()
                self.salud = int(lineas[1].strip())
                self.fuerza = int(lineas[2].strip())
            print("📜 Partida cargada exitosamente.")
        except FileNotFoundError:
            print("⚠️ No hay partida guardada previa.")

# Prueba de persistencia
jugador = Jugador("Itza")
jugador.guardar_partida()
jugador.cargar_partida()