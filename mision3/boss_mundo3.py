comerciante = input("Nombre del comerciante: ")
esmeraldas = int(input("¿Cuántas esmeraldas tienes en total?: "))
cantidad_items = int(input("¿Cuántos ítems vas a comprar?: "))
precio = float(input("Precio de cada ítem (en esmeraldas): "))

# Cálculos
costo_total = cantidad_items * precio
restante = esmeraldas - costo_total

# Resumen de Transacción con f-strings
print("\n--- RESUMEN DEL COMERCIO ---")
print(f"Comerciante: {comerciante}")
print(f"Costo total de la compra: {costo_total} esmeraldas")
print(f"Esmeraldas restantes: {restante}")