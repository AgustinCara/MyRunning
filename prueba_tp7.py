# TP7 - Pruebas del grafo de recorridos

from Index import Recorrido
from grafo_recorridos import GrafoRecorridos

grafo = GrafoRecorridos()

# Creamos recorridos de prueba
r1 = Recorrido(1, "Parque Finky", 3.0, "Fácil")
r2 = Recorrido(2, "Parque Finky", 5.0, "Media")
r3 = Recorrido(3, "Parque de Lomas", 7.0, "Media")
r4 = Recorrido(4, "Recorrido de prueba", 10.0, "Media")

# Agregamos los vertices
grafo.agregar_vertice(r1)
grafo.agregar_vertice(r2)
grafo.agregar_vertice(r3)
grafo.agregar_vertice(r4)

# Generamos las conexiones
grafo.conectar_por_distancia()

print("Cantidad de vertices:", len(grafo.vertices))

print("\n--- LISTA DE ADYACENCIA ---")

for id_recorrido in grafo.adyacencia:
    print(id_recorrido, "->", grafo.adyacencia[id_recorrido])

# Comprobamos las conexiones
assert grafo.adyacencia[1] == [2]
assert grafo.adyacencia[2] == [1, 3]
assert grafo.adyacencia[3] == [2]
assert grafo.adyacencia[4] == []

print("\nTodas las pruebas fueron exitosas.")