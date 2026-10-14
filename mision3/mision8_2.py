# Cargar la bitácora espacial desde el disco
with open("bitacora_nave.txt", "r") as bitacora:
    registro = bitacora.read()

print("🛰️ RECUPERANDO INFORMACIÓN DE VUELO:")
print(registro)