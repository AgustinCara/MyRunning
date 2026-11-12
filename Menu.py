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


# Cargamos los recorridos en el arbol
arbol = ArbolRecorridos()

for i, r in enumerate(recorridos):
    recorrido = Index.Recorrido(
        i + 1,
        r["nombre"],
        r["distancia"],
        r["dificultad"]
    )
    arbol.insertar(recorrido)


# Cargamos las categorias en el arbol general: Recorridos > Dificultad > Lugar > Distancia
categorias = ArbolGeneral("Recorridos")

for recorrido in arbol.inorden():
    nodo_dificultad = categorias.raiz.buscar_hijo(recorrido.dificultad)
    if nodo_dificultad is None:
        nodo_dificultad = categorias.raiz.agregar_hijo(NodoGeneral(recorrido.dificultad))

    nodo_lugar = nodo_dificultad.buscar_hijo(recorrido.nombre)
    if nodo_lugar is None:
        nodo_lugar = nodo_dificultad.agregar_hijo(NodoGeneral(recorrido.nombre))

    nodo_lugar.agregar_hijo(NodoGeneral(str(recorrido.distancia_km) + " km", recorrido))

# Menú principal
while True:
    print("\n=== MY RUNNING ===")
    print("1. Registrar entrenamiento")
    print("2. Ver estadísticas")
    print("3. Buscar recorridos")
    print("4. Próximas carreras")
    print("5. Explorar categorías")
    print("6. Ranking de mejores ritmos")
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


    # 5. Explorar categorías con el arbol general
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

    # 0. Salir
    elif opcion == "0":
        print("¡Hasta luego!")
        break

    else:
        print("Opción inválida, intentá de nuevo.")
