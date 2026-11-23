from grafo_recorridos import GrafoRecorridos
import Index
from arbol_recorridos import ArbolRecorridos
from arbol_general import ArbolGeneral, NodoGeneral
from heap_entrenamientos import HeapEntrenamientos
from Index import Entrenamiento

def mostrar_ritmo(ritmo):
    segundos_totales = round(ritmo * 60)
    minutos = segundos_totales // 60
    segundos = segundos_totales % 60

    return f"{minutos}:{segundos:02d}"

entrenamientos = [
    {"fecha": "01/09/2026", "distancia": 5.0, "tiempo": 34.8, "lugar": "Parque Municipal"},
    {"fecha": "04/09/2026", "distancia": 10.0, "tiempo": 72.6, "lugar": "Costanera"}
]


recorridos = [
    {"nombre": "Quinta Rocca - UNaB", "distancia": 2.0, "dificultad": "Fácil"},
    {"nombre": "Quinta Rocca - UNaB", "distancia": 3.0, "dificultad": "Fácil"},
    {"nombre": "Parque Finky", "distancia": 3.0, "dificultad": "Fácil"},
    {"nombre": "Parque Finky", "distancia": 5.0, "dificultad": "Media"},
    {"nombre": "Parque de Lomas", "distancia": 5.0, "dificultad": "Fácil"},
    {"nombre": "Parque de Lomas", "distancia": 7.0, "dificultad": "Media"},
    {"nombre": "Polideportivo de Burzaco", "distancia": 3.0, "dificultad": "Fácil"},
    {"nombre": "Polideportivo de Burzaco", "distancia": 5.0, "dificultad": "Media"},
    {"nombre": "Parque Ramón Carrillo", "distancia": 2.7, "dificultad": "Fácil"},
    {"nombre": "Parque Ramón Carrillo", "distancia": 5.0, "dificultad": "Media"},
    {"nombre": "Plaza Brown - Adrogué", "distancia": 2.0, "dificultad": "Fácil"},
    {"nombre": "Plaza Brown - Adrogué", "distancia": 3.0, "dificultad": "Fácil"},
    {"nombre": "Circuito urbano de Longchamps", "distancia": 8.0, "dificultad": "Media"}
]


# Cargamos los recorridos en el arbol y en el grafo
arbol = ArbolRecorridos()
grafo = GrafoRecorridos()

for i, r in enumerate(recorridos):
    recorrido = Index.Recorrido(
        i + 1,
        r["nombre"],
        r["distancia"],
        r["dificultad"]
    )
    arbol.insertar(recorrido)
    grafo.agregar_vertice(recorrido)

# TP7 - Conectamos los recorridos
grafo.conectar_por_distancia()

# TP5 - Árbol general de categorías
categorias = ArbolGeneral("Recorridos")

for recorrido in arbol.inorden():
    nodo_dificultad = categorias.raiz.buscar_hijo(recorrido.dificultad)

    if nodo_dificultad is None:
        nodo_dificultad = categorias.raiz.agregar_hijo(
            NodoGeneral(recorrido.dificultad)
        )

    nodo_lugar = nodo_dificultad.buscar_hijo(recorrido.nombre)

    if nodo_lugar is None:
        nodo_lugar = nodo_dificultad.agregar_hijo(
            NodoGeneral(recorrido.nombre)
        )

    nodo_lugar.agregar_hijo(
        NodoGeneral(str(recorrido.distancia_km) + " km", recorrido)
    )

# Menú principal
while True:
    print("\n=== MY RUNNING ===")
    print("1. Registrar entrenamiento")
    print("2. Ver estadísticas")
    print("3. Buscar recorridos")
    print("4. Próximas carreras")
    print("5. Explorar categorías")
    print("6. Ranking de mejores ritmos")
    print("7. Recomendar recorridos")
    print("8. Explorar conexiones entre recorridos")
    print("9. Buscar progresión de menor costo")
    print("0. Salir")
    
    opcion = input("Seleccione una opción: ")

    # 1. Registrar
    if opcion == "1":
        fecha = input("Fecha (DD/MM/AAAA): ")
        distancia = float(input("Distancia en km: "))
        tiempo = float(input("Tiempo en min: "))
        lugar = input("Lugar: ")

        nuevo = {"fecha": fecha, "distancia": distancia, "tiempo": tiempo, "lugar": lugar}
        entrenamientos.append(nuevo)
        print("¡Entrenamiento guardado con éxito!")

    # 2. Ver Estadísticas (Sumar y Contar)
    elif opcion == "2":
        print("\n--- MIS ESTADÍSTICAS ---")
        total_km = 0
        for e in entrenamientos:
            total_km = total_km + e["distancia"]

        print("Total de entrenamientos:", len(entrenamientos))
        print("Kilómetros totales:", total_km, "km")

    # 3. Buscar recorridos con el arbol
    elif opcion == "3":
        print("\n--- BUSCAR RECORRIDOS ---")
        dist_deseada = float(input("¿Cuántos km querés correr?: "))

        encontrados = arbol.buscar(dist_deseada)

        if encontrados:
            print("Recorridos encontrados:")
            for r in encontrados:
                print("-", r.nombre, "(", r.distancia_km, "km ) -", r.dificultad)
        else:
            print("No hay recorridos con esa distancia exacta.")


    # 4. Próximas Carreras
    elif opcion == "4":
        print("\n--- PRÓXIMAS CARRERAS ---")
        print("1. Circuito de las Estaciones - Verano")
        print("   Fecha: 20/12/2026")
        print("   Distancia: 10 km")
        print("   Lugar: Av. Figueroa Alcorta y Av. Monroe, CABA")

        print("\n2. San Silvestre Buenos Aires Carnaval")
        print("   Fecha: 31/12/2026")
        print("   Distancia: 8 km")
        print("   Lugar: Av. 9 de Julio y Perón, CABA")


    # 5. Explorar categorías con el árbol general
    elif opcion == "5":
        while True:
            print("\n--- EXPLORAR CATEGORÍAS ---")
            print("1. Ver árbol completo")
            print("2. Buscar categoría o lugar")
            print("3. Ver recorridos del árbol")
            print("0. Volver")

            sub_opcion = input("Seleccione una opción: ")

            if sub_opcion == "1":
                print()
                print(categorias.mostrar())

            elif sub_opcion == "2":
                texto = input("¿Qué querés buscar? (ej: Media, Finky): ")
                encontrados = categorias.buscar(texto)

                if encontrados:
                    for nodo in encontrados:
                        print("\n" + " > ".join(categorias.camino(nodo)))
                        for r in categorias.recorridos_de(nodo):
                            print("   -", r.nombre, "(", r.distancia_km, "km ) -", r.dificultad)
                else:
                    print("No se encontró ninguna categoría con ese nombre.")

            elif sub_opcion == "3":
                print("\nPreorden:", " -> ".join(categorias.preorden()))
                print("\nPostorden:", " -> ".join(categorias.postorden()))
                print("\nPor niveles:", " -> ".join(categorias.por_niveles()))
                print("\nAltura del árbol:", categorias.altura())
                print("Cantidad de nodos:", categorias.cantidad_nodos())

            elif sub_opcion == "0":
                break

            else:
                print("Opción inválida, intentá de nuevo.")

    # 6. Ranking de mejores ritmos
    elif opcion == "6":
        print("\n--- TOP 3 MEJORES RITMOS ---")

        heap = HeapEntrenamientos()

        for i, e in enumerate(entrenamientos):
            entrenamiento = Entrenamiento(
                i + 1,
                e["fecha"],
                e["distancia"],
                e["tiempo"],
                0,
                e["lugar"]
            )

            if entrenamiento.distancia_km > 0:
                heap.insertar(entrenamiento)

        for puesto in range(1, 4):
            mejor = heap.extraer_mejor()

            if mejor is None:
                break

            print(
    puesto, "-",
    mejor.lugar,
    "- Distancia:", mejor.distancia_km, "km",
    "- Ritmo:", mostrar_ritmo(mejor.ritmo), "min/km"
)

    # 7. Recomendar recorridos con el grafo
    elif opcion == "7":
        print("\n--- RECOMENDAR RECORRIDOS ---")

        for r in grafo.vertices.values():
            print(r.id, "-", r.nombre, "-", r.distancia_km, "km")

        try:
            id_recorrido = int(input("\nSeleccione un recorrido: "))

            if id_recorrido in grafo.vertices:
                relacionados = grafo.vecinos(id_recorrido)

                if relacionados:
                    print("\nRecorridos recomendados:")

                    for r in relacionados:
                        print("-", r.nombre, "-", r.distancia_km, "km", "-", r.dificultad)
                else:
                    print("No hay recorridos relacionados.")
            else:
                print("El recorrido no existe.")

        except ValueError:
            print("Debe ingresar un número válido.")

    # 8. Exploracion de recorridos con BFS y DFS
    elif opcion == "8":
        print("\n--- EXPLORAR CONEXIONES ---")
        print("1. Buscar una progresion de recorridos (BFS)")
        print("2. Explorar recorridos conectados (DFS)")
        print("0. Volver")

        sub_opcion = input("Seleccione una opcion: ")

        if sub_opcion == "1" or sub_opcion == "2":

            for r in grafo.vertices.values():
                print(r.id, "-", r.nombre, "-", r.distancia_km, "km")

            try:
                inicio = int(input("\nSeleccione el recorrido inicial: "))

                if inicio not in grafo.vertices:
                    print("El recorrido no existe.")

                elif sub_opcion == "1":
                    destino = int(input("Seleccione el recorrido final: "))

                    camino = grafo.bfs(inicio, destino)

                    if camino:
                        print("\n--- PROGRESION DE RECORRIDOS ---")

                        for id_recorrido in camino:
                            r = grafo.vertices[id_recorrido]
                            print("-", r.nombre, "-", r.distancia_km, "km")

                        print("Cantidad de conexiones:", len(camino) - 1)
                    else:
                        print("No existe un camino entre los recorridos.")

                elif sub_opcion == "2":
                    resultado = grafo.dfs(inicio)

                    print("\n--- RECORRIDOS CONECTADOS ---")

                    for id_recorrido in resultado:
                        r = grafo.vertices[id_recorrido]
                        print("-", r.nombre, "-", r.distancia_km, "km")

                    print("Total de recorridos visitados:", len(resultado))

            except ValueError:
                print("Debe ingresar un numero valido.")

        elif sub_opcion != "0":
            print("Opcion invalida.")
  
    # 9. Buscar progresión de menor costo con Dijkstra
    elif opcion == "9":
        print("\n--- PROGRESIÓN DE MENOR COSTO ---")

        for r in grafo.vertices.values():
            print(r.id, "-", r.nombre, "-", r.distancia_km, "km")

        try:
            inicio = int(input("\nSeleccione el recorrido inicial: "))
            destino = int(input("Seleccione el recorrido final: "))

            camino, costo = grafo.dijkstra(inicio, destino)

            if camino:
                print("\n--- CAMINO ENCONTRADO ---")

                for id_recorrido in camino:
                    r = grafo.vertices[id_recorrido]
                    print("-", r.nombre, "-", r.distancia_km, "km")

                print("Costo total:", round(costo, 2), "km de diferencia acumulada")
            else:
                print("No existe un camino entre los recorridos.")

        except ValueError:
            print("Debe ingresar un número válido.")

    # 0. Salir
    elif opcion == "0":
        print("¡Hasta luego!")
        break

    else:
        print("Opción inválida, intentá de nuevo.")
