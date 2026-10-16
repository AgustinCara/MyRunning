from arbol_recorridos import ArbolRecorridos
from Index import Recorrido

arbol = ArbolRecorridos()

distancias = [3, 5, 8]

for i, distancia in enumerate(distancias):
    recorrido = Recorrido(i + 1, "Recorrido de prueba", distancia, "Fácil")
    arbol.insertar(recorrido)
    print("Raíz:", arbol.raiz.recorridos[0].distancia_km)
print("Derecha:", arbol.raiz.derecha.recorridos[0].distancia_km)
print("Derecha de derecha:", arbol.raiz.derecha.derecha.recorridos[0].distancia_km)