import heapq

def dijkstra(grafo, inicio):
    """
    Encuentra la distancia más corta desde un nodo
    hasta todos los demás nodos.
    Utilizamos una cola de prioridad mediante heapq.
    """

    # Al principio todas las distancias son infinitas.
    distancias = {
        nodo: float("inf")
        for nodo in grafo
    }

    # La distancia desde el inicio hasta sí mismo es 0.
    distancias[inicio] = 0

    # Guardamos los nodos anteriores para poder reconstruir
    # el camino posteriormente.
    anteriores = {
        nodo: None
        for nodo in grafo
    }

    # Cola de prioridad.
    # Guarda: (distancia, nodo)
    cola = [(0, inicio)]

    while cola:

        distancia_actual, nodo_actual = heapq.heappop(cola)

        # Si encontramos una distancia anterior mejor,
        # ignoramos esta información.
        if distancia_actual > distancias[nodo_actual]:
            continue

        # Revisamos los vecinos del nodo actual.
        for vecino, peso in grafo[nodo_actual]:

            nueva_distancia = distancia_actual + peso

            # Si encontramos un camino más corto...
            if nueva_distancia < distancias[vecino]:

                # Actualizamos la distancia.
                distancias[vecino] = nueva_distancia

                # Guardamos de dónde venimos.
                anteriores[vecino] = nodo_actual

                # Agregamos el nuevo camino a la cola.
                heapq.heappush(
                    cola,
                    (nueva_distancia, vecino)
                )

    return distancias, anteriores


def reconstruir_ruta(anteriores, inicio, destino):
#    Reconstruye el camino desde inicio hasta destino.

    ruta = []

    actual = destino

    while actual is not None:

        ruta.append(actual)

        if actual == inicio:
            break

        actual = anteriores[actual]

    # Si no pudimos llegar al inicio,
    # significa que no existe una ruta.
    if ruta[-1] != inicio:
        return []

    # La ruta estaba al revés.
    ruta.reverse()

    return ruta