import time
from busquedas import busqueda_secuencial, busqueda_binaria


# Recorrido simple para hacer las pruebas del TP2
class Recorrido:
    def __init__(self, id_recorrido, nombre, distancia_km, dificultad):
        self.id = id_recorrido
        self.nombre = nombre
        self.distancia_km = distancia_km
        self.dificultad = dificultad


# Crea recorridos de prueba
def crear_recorridos(cantidad):
    recorridos = []

    for i in range(cantidad):
        recorrido = Recorrido(i, "Recorrido " + str(i), float(i + 1), "Media")
        recorridos.append(recorrido)

    return recorridos


# Prueba las dos busquedas con diferentes cantidades de recorridos
cantidades = [100, 1000, 10000]

for cantidad in cantidades:

    recorridos = crear_recorridos(cantidad)

    # Buscamos el ultimo recorrido para probar el peor caso
    distancia_buscada = float(cantidad)

    inicio = time.perf_counter()
    busqueda_secuencial(recorridos, distancia_buscada)
    fin = time.perf_counter()

    tiempo_secuencial = (fin - inicio) * 1000

    inicio = time.perf_counter()
    busqueda_binaria(recorridos, distancia_buscada)
    fin = time.perf_counter()

    tiempo_binaria = (fin - inicio) * 1000

    print("Cantidad de recorridos:", cantidad)
    print("Busqueda secuencial:", tiempo_secuencial, "ms")
    print("Busqueda binaria:", tiempo_binaria, "ms")
    print("-----------------------------")
