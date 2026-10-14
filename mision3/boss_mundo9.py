# 1. Definición de la Clase Personaje con atributos y métodos
class Personaje:
    def __init__(self, nombre, vida, fuerza):
        self.nombre = nombre
        self.vida = vida
        self.fuerza = fuerza

    def atacar(self, enemigo):
        enemigo.vida -= self.fuerza
        print(f"⚔️ {self.nombre} atacó a {enemigo.nombre} causando {self.fuerza} de daño. Vida de {enemigo.nombre}: {enemigo.vida}")

    def curar(self, pocion):
        self.vida += pocion
        print(f"🧪 {self.nombre} se curó +{pocion} de vida. Vida actual: {self.vida}")

# 2. Creación de instancias e interacción (fuera de la clase)
jugador = Personaje("Itza", 100, 35)
boss = Personaje("Wither 💀", 200, 20)