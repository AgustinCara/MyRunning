# TP6 - Comparacion de Heap y ordenamiento tradicional

import time
import statistics
from Index import Entrenamiento
from heap_entrenamientos import HeapEntrenamientos

# Creamos 1000 entrenamientos ficticios
entrenamientos = []

for i in range(10000):
    distancia = 5 + (i % 10)
    tiempo = distancia * (5 + (i % 20) / 10)

    entrenamiento = Entrenamiento(
        i + 1,
        "04/11/2026",
        distancia,
        tiempo,
        0,
        "Entrenamiento de prueba"
    )

    entrenamientos.append(entrenamiento)

print("Cantidad de entrenamientos:", len(entrenamientos))

# Medimos el tiempo de nuestra Heap
inicio = time.perf_counter()

heap = HeapEntrenamientos()

for entrenamiento in entrenamientos:
    heap.insertar(entrenamiento)

top_3 = []

for i in range(3):
    mejor = heap.extraer_mejor()
    top_3.append(mejor)

fin = time.perf_counter()

tiempo_heap = fin - inicio

print("\n--- RESULTADOS HEAP ---")
print("Tiempo:", tiempo_heap, "segundos")

for entrenamiento in top_3:
    print(
        "Entrenamiento:", entrenamiento.id,
        "- Ritmo:", round(entrenamiento.ritmo, 2), "min/km"
    )

# Medimos el ordenamiento tradicional
inicio = time.perf_counter()

ordenados = sorted(
    entrenamientos,
    key=lambda entrenamiento: entrenamiento.ritmo
)

top_3_ordenados = ordenados[:3]

fin = time.perf_counter()

tiempo_ordenamiento = fin - inicio

print("\n--- RESULTADOS ORDENAMIENTO ---")
print("Tiempo:", tiempo_ordenamiento, "segundos")

for entrenamiento in top_3_ordenados:
    print(
        "Entrenamiento:", entrenamiento.id,
        "- Ritmo:", round(entrenamiento.ritmo, 2), "min/km"
    )

print("\n--- CONCLUSION DEL EXPERIMENTO ---")
print("Ambos metodos encontraron los mejores ritmos.")
print("El orden puede variar cuando hay entrenamientos empatados.")
print("La Heap permite insertar nuevos datos y extraer el mejor.")
print("Los tiempos medidos dependen de la implementacion y del equipo.")

# TP6 - Comparacion con 5 repeticiones

tiempos_heap = []
tiempos_ordenamiento = []

for repeticion in range(5):

    # Medimos nuestra Heap
    inicio = time.perf_counter()

    heap = HeapEntrenamientos()

    for entrenamiento in entrenamientos:
        heap.insertar(entrenamiento)

    for i in range(3):
        heap.extraer_mejor()

    fin = time.perf_counter()
    tiempos_heap.append(fin - inicio)

    # Medimos el ordenamiento tradicional
    inicio = time.perf_counter()

    ordenados = sorted(
        entrenamientos,
        key=lambda entrenamiento: entrenamiento.ritmo
    )

    top_3 = ordenados[:3]

    fin = time.perf_counter()
    tiempos_ordenamiento.append(fin - inicio)


print("\n--- PROMEDIO DE 5 REPETICIONES ---")
print("Heap:", statistics.mean(tiempos_heap), "segundos")
print("Ordenamiento:", statistics.mean(tiempos_ordenamiento), "segundos")