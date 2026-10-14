Guardamos la bitácora de vuelo de la nave
with open("bitacora_nave.txt", "w") as bitacora:
    bitacora.write("Nave: Apolo-11\n")
    bitacora.write("Estado: En órbita\n")
    bitacora.write("Combustible: 100%\n")

print("💾 Bitácora espacial guardada con éxito.")