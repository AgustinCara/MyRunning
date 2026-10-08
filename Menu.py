import Index
from arbol_recorridos import ArbolRecorridos

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

# Menú principal
while True:
    print("\n=== MY RUNNING ===")
    print("1. Registrar entrenamiento")
    print("2. Ver estadísticas")
    print("3. Buscar recorridos")
    print("4. Próximas carreras")
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
        print("1. Maratón de la Ciudad (21 km) - 15/10/2026")
        print("2. Carrera de las Luces (10 km) - 02/11/2026")

    # 0. Salir
    elif opcion == "0":
        print("¡Hasta luego!")
        break

    else:
        print("Opción inválida, intentá de nuevo.")
