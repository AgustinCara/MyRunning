# TP8 - Pruebas de BFS y DFS

from Index import Recorrido
from grafo_recorridos import GrafoRecorridos

grafo = GrafoRecorridos()

# Creamos recorridos de prueba
r1 = Recorrido(1, "Parque Finky", 3.0, "Fácil")
r2 = Recorrido(2, "Parque Finky", 5.0, "Media")
r3 = Recorrido(3, "Parque de Lomas", 5.0, "Fácil")
r4 = Recorrido(4, "Parque de Lomas", 7.0, "Media")
r5 = Recorrido(5, "Longchamps", 8.0, "Media")
r6 = Recorrido(6, "Recorrido aislado", 11.0, "Media")

for r in [r1, r2, r3, r4, r5, r6]:
    grafo.agregar_vertice(r)

grafo.conectar_por_distancia()

# Prueba BFS
print("--- PRUEBAS BFS ---")

camino = grafo.bfs(1, 5)
print("Camino encontrado:", camino)
print("Cantidad de conexiones:", len(camino) - 1)

assert camino == [1, 2, 4, 5]
assert grafo.bfs(1, 6) == []
assert grafo.bfs(1, 1) == [1]
assert grafo.bfs(1, 99) == []

# Prueba DFS
print("\n--- PRUEBAS DFS ---")

resultado = grafo.dfs(1)
print("Orden de visita:", resultado)
print("Cantidad de vertices visitados:", len(resultado))

assert resultado == [1, 2, 3, 4, 5]
assert grafo.dfs(6) == [6]
assert grafo.dfs(99) == []

print("\nTodas las pruebas fueron exitosas.")
