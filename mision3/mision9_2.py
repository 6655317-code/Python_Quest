class NaveEspacial:
    def __init__(self, modelo, combustible):
        self.modelo = modelo
        self.combustible = combustible

    def acelerar(self, consumo):
        self.combustible -= consumo
        print(f"🚀 {self.modelo} aceleró. Combustible restante: {self.combustible}L")

nave1 = NaveEspacial("Apolo-11", 100)
nave1.acelerar(20)