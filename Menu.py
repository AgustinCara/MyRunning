import Index

entrenamientos = [
    {"fecha": "01/09/2026", "distancia": 5.0, "tiempo": 34.8, "lugar": "Parque Municipal"},
    {"fecha": "04/09/2026", "distancia": 10.0, "tiempo": 72.6, "lugar": "Costanera"}
]

recorridos = [
    {"nombre": "Circuito Parque A", "distancia": 7.8, "dificultad": "Fácil"},
    {"nombre": "Circuito Costanera", "distancia": 8.2, "dificultad": "Media"},
    {"nombre": "Reserva Ecológica", "distancia": 10.5, "dificultad": "Media"}
]

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

    # 3. Buscar / Filtrar Recorridos
    elif opcion == "3":
        print("\n--- BUSCAR RECORRIDOS ---")
        dist_deseada = float(input("¿Cuántos km querés correr?: "))
        
        print("Recorridos recomendados (cerca de tu objetivo):")
        for r in recorridos:
            # Muestra los que estén a +/- 2 km de diferencia
            if abs(r["distancia"] - dist_deseada) <= 2.0:
                print("-", r["nombre"], "(", r["distancia"], "km ) -", r["dificultad"])

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