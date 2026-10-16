# TP4 - Arbol AVL de recorridos

class NodoAVL:
    def __init__(self, recorrido):
        self.recorridos = [recorrido]
        self.izquierda = None
        self.derecha = None
        self.altura = 1


class ArbolAVL:
    def __init__(self):
        self.raiz = None

    def obtener_altura(self, nodo):
        if nodo is None:
            return 0
        return nodo.altura

    def calcular_equilibrio(self, nodo):
        if nodo is None:
            return 0

        altura_izquierda = self.obtener_altura(nodo.izquierda)
        altura_derecha = self.obtener_altura(nodo.derecha)

        return altura_izquierda - altura_derecha

    def rotar_izquierda(self, nodo):
        nuevo = nodo.derecha
        nodo.derecha = nuevo.izquierda
        nuevo.izquierda = nodo

        nodo.altura = 1 + max(
            self.obtener_altura(nodo.izquierda),
            self.obtener_altura(nodo.derecha)
        )

        nuevo.altura = 1 + max(
            self.obtener_altura(nuevo.izquierda),
            self.obtener_altura(nuevo.derecha)
        )

        return nuevo

    def rotar_derecha(self, nodo):
        nuevo = nodo.izquierda
        nodo.izquierda = nuevo.derecha
        nuevo.derecha = nodo

        nodo.altura = 1 + max(
            self.obtener_altura(nodo.izquierda),
            self.obtener_altura(nodo.derecha)
        )

        nuevo.altura = 1 + max(
            self.obtener_altura(nuevo.izquierda),
            self.obtener_altura(nuevo.derecha)
        )

        return nuevo

    def insertar(self, recorrido):
        self.raiz = self._insertar(self.raiz, recorrido)

    def _insertar(self, nodo, recorrido):
        if nodo is None:
            return NodoAVL(recorrido)

        if recorrido.distancia_km < nodo.recorridos[0].distancia_km:
            nodo.izquierda = self._insertar(nodo.izquierda, recorrido)

        elif recorrido.distancia_km > nodo.recorridos[0].distancia_km:
            nodo.derecha = self._insertar(nodo.derecha, recorrido)

        else:
            nodo.recorridos.append(recorrido)
            return nodo    
        nodo.altura = 1 + max(
            self.obtener_altura(nodo.izquierda),
            self.obtener_altura(nodo.derecha)
        )

        equilibrio = self.calcular_equilibrio(nodo)
        # Si el árbol está cargado hacia la izquierda
        if equilibrio > 1:
            if recorrido.distancia_km > nodo.izquierda.recorridos[0].distancia_km:
                nodo.izquierda = self.rotar_izquierda(nodo.izquierda)

            return self.rotar_derecha(nodo)

        # Si el árbol está cargado hacia la derecha
        if equilibrio < -1:
            if recorrido.distancia_km < nodo.derecha.recorridos[0].distancia_km:
                nodo.derecha = self.rotar_derecha(nodo.derecha)

            return self.rotar_izquierda(nodo)

        return nodo
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