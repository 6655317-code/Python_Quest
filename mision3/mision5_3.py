# Misión 5.3 - Acumuladores y Sumatorias
total_esmeraldas = 0

for aldeano in range(1, 4):
    obtenidas = int(input(f"¿Cuántas esmeraldas te dio el aldeano {aldeano}?: "))
    total_esmeraldas = total_esmeraldas + obtenidas

print(f"¡Comercio finalizado! Conseguiste un total de {total_esmeraldas} esmeraldas.")