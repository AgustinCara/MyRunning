# TP2 - Comparacion de busquedas de recorridos por distancia


# Busca recorriendo la lista uno por uno
def busqueda_secuencial(recorridos, distancia_buscada):
    for recorrido in recorridos:
        if recorrido.distancia_km == distancia_buscada:
            return recorrido

    return None


# Busca dividiendo la lista ordenada en partes
def busqueda_binaria(recorridos, distancia_buscada):
    inicio = 0
    fin = len(recorridos) - 1

    while inicio <= fin:
        medio = (inicio + fin) // 2

        if recorridos[medio].distancia_km == distancia_buscada:
            return recorridos[medio]

        elif recorridos[medio].distancia_km < distancia_buscada:
            inicio = medio + 1

        else:
            fin = medio - 1

    return None
