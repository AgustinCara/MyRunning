from arbol_general import ArbolGeneral, NodoGeneral


class Recorrido:
    def __init__(self, nombre, distancia_km):
        self.nombre = nombre
        self.distancia_km = distancia_km


arbol = ArbolGeneral("Recorridos")

facil = arbol.raiz.agregar_hijo(NodoGeneral("Fácil"))
media = arbol.raiz.agregar_hijo(NodoGeneral("Media"))

plaza = facil.agregar_hijo(NodoGeneral("Plaza"))
plaza.agregar_hijo(NodoGeneral("2 km", Recorrido("Plaza", 2)))
plaza.agregar_hijo(NodoGeneral("3 km", Recorrido("Plaza", 3)))

parque = media.agregar_hijo(NodoGeneral("Parque"))
parque.agregar_hijo(NodoGeneral("5 km", Recorrido("Parque", 5)))

print(arbol.mostrar())

print("\nBusqueda de 'plaza':")
for nodo in arbol.buscar("plaza"):
    print(" > ".join(arbol.camino(nodo)))

print("\nRecorridos dentro de Fácil:")
for recorrido in arbol.recorridos_de(facil):
    print(recorrido.nombre, recorrido.distancia_km)

print("\nPreorden:", arbol.preorden())
print("Postorden:", arbol.postorden())
print("Por niveles:", arbol.por_niveles())
print("Altura:", arbol.altura())
print("Cantidad de nodos:", arbol.cantidad_nodos())
