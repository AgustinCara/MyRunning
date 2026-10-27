# TP5 - Arbol general (n-ario) de categorias
from collections import deque


class NodoGeneral:
    def __init__(self, nombre, recorrido=None):
        self.nombre = nombre
        self.recorrido = recorrido  # Solo las hojas guardan un recorrido
        self.hijos = []

    def agregar_hijo(self, hijo):
        self.hijos.append(hijo)
        return hijo

    # Busca un hijo directo por su nombre
    def buscar_hijo(self, nombre):
        for hijo in self.hijos:
            if hijo.nombre == nombre:
                return hijo
        return None

    def es_hoja(self):
        return len(self.hijos) == 0


class ArbolGeneral:
    def __init__(self, nombre_raiz):
        self.raiz = NodoGeneral(nombre_raiz)

    # Busca todos los nodos cuyo nombre contenga el texto (recorrido en profundidad)
    def buscar(self, texto):
        texto = texto.lower()
        encontrados = []

        def recorrer(nodo):
            if texto in nodo.nombre.lower():
                encontrados.append(nodo)
            for hijo in nodo.hijos:
                recorrer(hijo)

        recorrer(self.raiz)
        return encontrados

    # Devuelve los nombres desde la raiz hasta el nodo buscado
    def camino(self, objetivo):
        ruta = []

        def recorrer(nodo):
            ruta.append(nodo.nombre)
            if nodo is objetivo:
                return True
            for hijo in nodo.hijos:
                if recorrer(hijo):
                    return True
            ruta.pop()
            return False

        recorrer(self.raiz)
        return ruta

    # Junta todos los recorridos que hay debajo de un nodo
    def recorridos_de(self, nodo):
        resultado = []

        def recorrer(nodo):
            if nodo.recorrido is not None:
                resultado.append(nodo.recorrido)
            for hijo in nodo.hijos:
                recorrer(hijo)

        recorrer(nodo)
        return resultado

    # Recorre el arbol en distintos ordenes
    def preorden(self):
        resultado = []

        def recorrer(nodo):
            resultado.append(nodo.nombre)
            for hijo in nodo.hijos:
                recorrer(hijo)

        recorrer(self.raiz)
        return resultado

    def postorden(self):
        resultado = []

        def recorrer(nodo):
            for hijo in nodo.hijos:
                recorrer(hijo)
            resultado.append(nodo.nombre)

        recorrer(self.raiz)
        return resultado

    def por_niveles(self):
        resultado = []
        cola = deque([self.raiz])

        while cola:
            nodo = cola.popleft()
            resultado.append(nodo.nombre)
            for hijo in nodo.hijos:
                cola.append(hijo)

        return resultado

    def altura(self):
        def calcular(nodo):
            if nodo.es_hoja():
                return 1
            return 1 + max(calcular(hijo) for hijo in nodo.hijos)

        return calcular(self.raiz)

    def cantidad_nodos(self):
        return len(self.preorden())

    # Dibuja el arbol con lineas, a partir del nodo indicado
    def mostrar(self, nodo=None):
        if nodo is None:
            nodo = self.raiz

        lineas = [nodo.nombre]

        def recorrer(nodo, prefijo):
            for i, hijo in enumerate(nodo.hijos):
                es_ultimo = i == len(nodo.hijos) - 1
                conector = "└── " if es_ultimo else "├── "
                lineas.append(prefijo + conector + hijo.nombre)
                recorrer(hijo, prefijo + ("    " if es_ultimo else "│   "))

        recorrer(nodo, "")
        return "\n".join(lineas)
