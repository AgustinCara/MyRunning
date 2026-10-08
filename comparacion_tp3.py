
import time
import random
from busquedas import busqueda_secuencial
from arbol_recorridos import ArbolRecorridos


class Recorrido:
    def __init__(self, nombre, distancia_km):
        self.nombre = nombre
        self.distancia_km = distancia_km


# Creamos recorridos de prueba
def crear_recorridos(cantidad):
    recorridos = []

    for i in range(cantidad):
        recorrido = Recorrido("Recorrido " + str(i), float(i + 1))
        recorridos.append(recorrido)

    return recorridos


# Comparamos las dos busquedas
cantidades = [100, 1000, 10000]

for cantidad in cantidades:
    recorridos = crear_recorridos(cantidad)

    arbol = ArbolRecorridos()

    recorridos_mezclados = recorridos.copy()
    random.Random(42).shuffle(recorridos_mezclados)

    for recorrido in recorridos_mezclados:
        arbol.insertar(recorrido)

    distancia_buscada = float(cantidad)

    repeticiones = 1000

    inicio = time.perf_counter()

    for i in range(repeticiones):
        busqueda_secuencial(recorridos, distancia_buscada)

    tiempo_secuencial = (time.perf_counter() - inicio) * 1000 / repeticiones

    inicio = time.perf_counter()

    for i in range(repeticiones):
        arbol.buscar(distancia_buscada)

    tiempo_arbol = (time.perf_counter() - inicio) * 1000 / repeticiones

    print("Cantidad de recorridos:", cantidad)
    print("Busqueda secuencial:", round(tiempo_secuencial, 6), "ms")
    print("Busqueda con arbol:", round(tiempo_arbol, 6), "ms")
    print("-----------------------------")
