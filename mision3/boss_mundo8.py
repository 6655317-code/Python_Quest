# 1. Guardar la partida en modo escritura ("w")
with open("partida_minecraft.txt", "w") as archivo:
    archivo.write("Jugadora: Itza\n")
    archivo.write("Puntos: 750\n")

# 2. Intentar cargar la partida en modo lectura ("r") de forma segura
try:
    with open("partida_minecraft.txt", "r") as archivo:
        datos = archivo.read()
        print("📜 PARTIDA CARGADA CON ÉXITO:")
        print(datos)
except FileNotFoundError:
    print("⚠️ No se encontró el archivo de partida_minecraft.txt.")