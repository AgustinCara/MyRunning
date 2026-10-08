from arbol_recorridos import ArbolRecorridos


class Recorrido:
    def __init__(self, nombre, distancia_km):
        self.nombre = nombre
        self.distancia_km = distancia_km


arbol = ArbolRecorridos()

arbol.insertar(Recorrido("Bosque", 5))
arbol.insertar(Recorrido("Costanera", 3))
arbol.insertar(Recorrido("Parque", 8))
arbol.insertar(Recorrido("Lago", 6))
arbol.insertar(Recorrido("Plaza", 4))

print("Busqueda de recorridos de 6 km:")
for recorrido in arbol.buscar(6):
    print(recorrido.nombre)

print("Inorden:")
for recorrido in arbol.inorden():
    print(recorrido.distancia_km)

print("Preorden:")
for recorrido in arbol.preorden():
    print(recorrido.distancia_km)

print("Postorden:")
for recorrido in arbol.postorden():
    print(recorrido.distancia_km)
