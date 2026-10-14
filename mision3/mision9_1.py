class NaveEspacial:
    def __init__(self, modelo, velocidad):
        self.modelo = modelo
        self.velocidad = velocidad

nave_1 = NaveEspacial("Apolo-11", 28000)
print(f"🚀 Nave: {nave_1.modelo} | Velocidad: {nave_1.velocidad} km/h")