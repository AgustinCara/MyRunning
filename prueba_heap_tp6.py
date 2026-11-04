from Index import Entrenamiento
from heap_entrenamientos import HeapEntrenamientos

def mostrar_ritmo(ritmo):
    segundos_totales = round(ritmo * 60)
    minutos = segundos_totales // 60
    segundos = segundos_totales % 60

    return f"{minutos}:{segundos:02d}"


# TP6 - Prueba con entrenamientos reales
heap = HeapEntrenamientos()

entrenamientos = [
    Entrenamiento(1, "2026-11-03", 11.03, 82 + 29/60, 150, "Entrenamiento 1"),
    Entrenamiento(2, "2026-10-02", 8.02, 52 + 57/60, 154, "Entrenamiento 2"),
    Entrenamiento(3, "2026-06-07", 7.35, 48 + 53/60, 155, "Entrenamiento 3"),
    Entrenamiento(4, "2025-09-12", 8.07, 56 + 26/60, 153, "Entrenamiento 4"),
    Entrenamiento(5, "2026-06-08", 4.60, 34 + 31/60, 142, "Entrenamiento 5"),
    Entrenamiento(6, "2026-03-14", 8.03, 57 + 34/60, 145, "Entrenamiento 6"),
    Entrenamiento(7, "2026-04-12", 4.90, 30 + 28/60, 146, "Entrenamiento 7")
]

for entrenamiento in entrenamientos:
    heap.insertar(entrenamiento)

print("--- PRUEBA HEAP TP6 ---")

for entrenamiento in heap.datos:
    print(
        entrenamiento.lugar,
        "- Distancia:", entrenamiento.distancia_km,
        "km - Ritmo:", round(entrenamiento.ritmo, 2),
        "min/km"
    )

print("\nMEJOR RITMO EN LA RAIZ:")
print(heap.datos[0].lugar)
print(round(heap.datos[0].ritmo, 2), "min/km")

print("\n--- TOP 3 MEJORES RITMOS ---")

for puesto in range(1, 4):
    mejor = heap.extraer_mejor()

    print(
        puesto, "-",
        mejor.lugar,
        "- Distancia:", mejor.distancia_km, "km",
        "- Ritmo:", mostrar_ritmo(mejor.ritmo), "min/km"
    )



