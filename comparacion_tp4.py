# TP4 - Comparacion entre arbol binario y AVL
import time
from arbol_recorridos import ArbolRecorridos
from arbol_avl import ArbolAVL
from Index import Recorrido

arbol_binario = ArbolRecorridos()
arbol_avl = ArbolAVL()

distancias = [3, 5, 8, 10, 12, 15, 18]

for i, distancia in enumerate(distancias):
    recorrido = Recorrido(i + 1, "Recorrido de prueba", distancia, "Fácil")

    arbol_binario.insertar(recorrido)
    arbol_avl.insertar(recorrido)
def contar_pasos(arbol, distancia):
    nodo = arbol.raiz
    pasos = 0

    while nodo is not None:
        pasos = pasos + 1
        distancia_nodo = nodo.recorridos[0].distancia_km

        if distancia == distancia_nodo:
            return pasos
        elif distancia < distancia_nodo:
            nodo = nodo.izquierda
        else:
            nodo = nodo.derecha

    return pasos


print("Pasos árbol binario:", contar_pasos(arbol_binario, 18))
print("Pasos árbol AVL:", contar_pasos(arbol_avl, 18))
inicio = time.perf_counter()

for i in range(10000):
    arbol_binario.buscar(18)

fin = time.perf_counter()

print("Tiempo árbol binario:", round(fin - inicio, 6), "segundos")
inicio = time.perf_counter()

for i in range(10000):
    arbol_avl.buscar(18)

fin = time.perf_counter()

print("Tiempo árbol AVL:", round(fin - inicio, 6), "segundos")