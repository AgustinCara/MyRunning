# TP3 - Arbol binario de busqueda de recorridos

class Nodo:
    def __init__(self, recorrido):
        self.recorridos = [recorrido]
        self.izquierda = None
        self.derecha = None


class ArbolRecorridos:
    def __init__(self):
        self.raiz = None

    # Agrega un recorrido segun su distancia
    def insertar(self, recorrido):
        self.raiz = self._insertar(self.raiz, recorrido)

    def _insertar(self, nodo, recorrido):
        if nodo is None:
            return Nodo(recorrido)

        if recorrido.distancia_km < nodo.recorridos[0].distancia_km:
            nodo.izquierda = self._insertar(nodo.izquierda, recorrido)
        elif recorrido.distancia_km > nodo.recorridos[0].distancia_km:
            nodo.derecha = self._insertar(nodo.derecha, recorrido)
        else:
            nodo.recorridos.append(recorrido)

        return nodo

    # Busca recorridos por kilometros
    def buscar(self, distancia):
        nodo = self.raiz

        while nodo is not None:
            distancia_nodo = nodo.recorridos[0].distancia_km

            if distancia == distancia_nodo:
                return nodo.recorridos
            elif distancia < distancia_nodo:
                nodo = nodo.izquierda
            else:
                nodo = nodo.derecha

        return []

    # Recorre el arbol en distintos ordenes
    def inorden(self):
        resultado = []

        def recorrer(nodo):
            if nodo is not None:
                recorrer(nodo.izquierda)
                resultado.extend(nodo.recorridos)
                recorrer(nodo.derecha)

        recorrer(self.raiz)
        return resultado

    def preorden(self):
        resultado = []

        def recorrer(nodo):
            if nodo is not None:
                resultado.extend(nodo.recorridos)
                recorrer(nodo.izquierda)
                recorrer(nodo.derecha)

        recorrer(self.raiz)
        return resultado

    def postorden(self):
        resultado = []

        def recorrer(nodo):
            if nodo is not None:
                recorrer(nodo.izquierda)
                recorrer(nodo.derecha)
                resultado.extend(nodo.recorridos)

        recorrer(self.raiz)
        return resultado
