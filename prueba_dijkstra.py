
from grafo_recorridos import GrafoRecorridos
from Index import Recorrido

grafo = GrafoRecorridos()

# Creamos tres recorridos de prueba
r1 = Recorrido(1, "Recorrido A", 3.0, "Fácil")
r2 = Recorrido(2, "Recorrido B", 5.0, "Fácil")
r3 = Recorrido(3, "Recorrido C", 7.0, "Media")

# Agregamos los recorridos al grafo
grafo.agregar_vertice(r1)
grafo.agregar_vertice(r2)
grafo.agregar_vertice(r3)

# Conectamos los recorridos por distancia
grafo.conectar_por_distancia()

# Buscamos el camino de menor costo
camino, costo = grafo.dijkstra(1, 3)

print("Camino encontrado:", camino)
print("Costo total:", costo)
