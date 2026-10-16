from arbol_avl import ArbolAVL
from Index import Recorrido

arbol = ArbolAVL()

distancias = [3, 5, 8]

for i, distancia in enumerate(distancias):
    recorrido = Recorrido(i + 1, "Recorrido de prueba", distancia, "Fácil")
    arbol.insertar(recorrido)

print("Raíz:", arbol.raiz.recorridos[0].distancia_km)
print("Izquierda:", arbol.raiz.izquierda.recorridos[0].distancia_km)
print("Derecha:", arbol.raiz.derecha.recorridos[0].distancia_km)
print("\n--- BUSQUEDA EN EL AVL ---")

encontrados = arbol.buscar(8)

if encontrados:
    for recorrido in encontrados:
        print("Encontrado:", recorrido.nombre, "-", recorrido.distancia_km, "km")
else:
    print("No se encontraron recorridos")