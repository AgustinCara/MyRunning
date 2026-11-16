from collections import deque

# TP7 - Grafo de recorridos

class GrafoRecorridos:
    def __init__(self):
        self.vertices = {}
        self.adyacencia = {}

    # Agrega un recorrido al grafo
    def agregar_vertice(self, recorrido):
        if recorrido.id not in self.vertices:
            self.vertices[recorrido.id] = recorrido
            self.adyacencia[recorrido.id] = []

    # Conecta dos recorridos
    def agregar_arista(self, id1, id2):
        if id1 == id2:
            return

        if id1 in self.vertices and id2 in self.vertices:
            if id2 not in self.adyacencia[id1]:
                self.adyacencia[id1].append(id2)
                self.adyacencia[id2].append(id1)

    # Obtiene los recorridos relacionados
    def vecinos(self, id_recorrido):

        resultado = []

        for id_vecino in self.adyacencia.get(id_recorrido, []):
            resultado.append(self.vertices[id_vecino])

        return resultado

    # Conecta recorridos con distancias similares
    def conectar_por_distancia(self):
        recorridos = list(self.vertices.values())

        for i in range(len(recorridos)):
            for j in range(i + 1, len(recorridos)):
                r1 = recorridos[i]
                r2 = recorridos[j]

                diferencia = abs(r1.distancia_km - r2.distancia_km)

                if diferencia <= 2:
                    self.agregar_arista(r1.id, r2.id)

    # TP8 - Busqueda por anchura (BFS)
    def bfs(self, id_inicio, id_destino):
        if id_inicio not in self.vertices or id_destino not in self.vertices:
            return []

        cola = deque([id_inicio])
        padres = {id_inicio: None}

        while cola:
            actual = cola.popleft()

            if actual == id_destino:
                camino = []

                while actual is not None:
                    camino.append(actual)
                    actual = padres[actual]

                camino.reverse()
                return camino

            for vecino in self.adyacencia[actual]:
                if vecino not in padres:
                    padres[vecino] = actual
                    cola.append(vecino)

        return []

    # TP8 - Busqueda por profundidad (DFS)
    def dfs(self, id_inicio):
        if id_inicio not in self.vertices:
            return []

        visitados = set()
        resultado = []

        def explorar(actual):
            visitados.add(actual)
            resultado.append(actual)

            for vecino in self.adyacencia[actual]:
                if vecino not in visitados:
                    explorar(vecino)

        explorar(id_inicio)
        return resultado

