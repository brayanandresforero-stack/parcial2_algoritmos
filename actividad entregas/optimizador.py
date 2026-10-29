from mochila import mochila_01
from dijkstra import dijkstra, reconstruir_ruta


def ajustar_por_volumen(paquetes, capacidad_volumen):
    """
    La mochila principal trabaja con el peso.

    Después verificamos que los paquetes seleccionados
    también puedan entrar físicamente por volumen.

    Si se supera el volumen, quitamos primero
    los paquetes de menor prioridad.
    """

    seleccionados = paquetes.copy()

    volumen_total = sum(
        paquete.calcular_volumen()
        for paquete in seleccionados
    )

    while volumen_total > capacidad_volumen and seleccionados:

        # Buscamos el paquete con menor prioridad.
        paquete_menor = min(
            seleccionados,
            key=lambda paquete: paquete.prioridad
        )

        seleccionados.remove(paquete_menor)

        volumen_total -= paquete_menor.calcular_volumen()

    return seleccionados


def asignar_paquetes(vehiculos, paquetes):
    """
    Asigna paquetes a los vehículos.

    Para cada vehículo:
    1. Ejecutamos mochila.
    2. Revisamos el volumen.
    3. Asignamos los paquetes.
    4. Los paquetes utilizados salen de los disponibles.
    """

    paquetes_disponibles = paquetes.copy()

    for vehiculo in vehiculos:

        if not paquetes_disponibles:
            break

        # Ejecutamos programación dinámica.
        seleccionados = mochila_01(
            paquetes_disponibles,
            vehiculo.capacidad_peso
        )

        # Verificamos también el volumen.
        seleccionados = ajustar_por_volumen(
            seleccionados,
            vehiculo.capacidad_volumen
        )

        # Agregamos los paquetes al vehículo.
        for paquete in seleccionados:
            vehiculo.agregar_paquete(paquete)

        # Quitamos los paquetes ya asignados.
        paquetes_disponibles = [
            paquete
            for paquete in paquetes_disponibles
            if paquete not in seleccionados
        ]

    return paquetes_disponibles


def calcular_ruta_vehiculo(vehiculo, grafo):
    """
    Calcula una ruta para un vehículo.

    Utilizamos Dijkstra para calcular el camino
    más corto entre las diferentes ubicaciones.

    La estrategia utilizada es:
    desde la ubicación actual,
    visitar primero el destino más cercano.

    Esta es una heurística sencilla para el proyecto.
    """

    if not vehiculo.paquetes:
        return ["Bodega"], 0

    # Obtenemos los destinos sin repetir.
    destinos = []

    for paquete in vehiculo.paquetes:

        if paquete.destino not in destinos:
            destinos.append(paquete.destino)

    ruta_completa = ["Bodega"]

    ubicacion_actual = "Bodega"

    distancia_total = 0

    while destinos:

        # Ejecutamos Dijkstra desde la ubicación actual.
        distancias, anteriores = dijkstra(
            grafo,
            ubicacion_actual
        )

        # Buscamos el destino más cercano.
        destino_mas_cercano = min(
            destinos,
            key=lambda destino: distancias[destino]
        )

        # Reconstruimos el camino.
        camino = reconstruir_ruta(
            anteriores,
            ubicacion_actual,
            destino_mas_cercano
        )

        # Agregamos la distancia.
        distancia_total += distancias[destino_mas_cercano]

        # Evitamos repetir el nodo inicial del camino.
        ruta_completa.extend(camino[1:])

        # Ahora estamos en ese destino.
        ubicacion_actual = destino_mas_cercano

        # Lo eliminamos de los destinos pendientes.
        destinos.remove(destino_mas_cercano)

    # Finalmente regresamos a la bodega.
    distancias, anteriores = dijkstra(
        grafo,
        ubicacion_actual
    )

    camino_regreso = reconstruir_ruta(
        anteriores,
        ubicacion_actual,
        "Bodega"
    )

    if camino_regreso:
        distancia_total += distancias["Bodega"]

        ruta_completa.extend(
            camino_regreso[1:]
        )

    return ruta_completa, distancia_total


def ejecutar_optimizacion(vehiculos, paquetes, grafo):
    """
    Ejecuta todo el proceso de optimización.
    Primero:
    asigna los paquetes.
    Después:
    calcula la ruta de cada vehículo.
    """

    print("\n+++++++++++++++++++++++++++++++++++++++++++")
    print("       INICIANDO OPTIMIZACION")
    print("++++++++++++++++++++++++++++++++++++++++++++")

    paquetes_no_asignados = asignar_paquetes(
        vehiculos,
        paquetes
    )

    print("\nAsignacion de paquetes terminada.")

    for vehiculo in vehiculos:

        if vehiculo.paquetes:

            ruta, distancia = calcular_ruta_vehiculo(
                vehiculo,
                grafo
            )

            print("\n------------------------------------")
            print(f"Vehiculo: {vehiculo.codigo}")
            print(f"Tipo: {vehiculo.tipo}")

            print("\nPaquetes:")

            for paquete in vehiculo.paquetes:

                print(
                    f"- {paquete.codigo} | "
                    f"{paquete.peso} kg | "
                    f"{paquete.destino}"
                )

            print(
                f"\nPeso utilizado: "
                f"{vehiculo.peso_utilizado()} kg"
            )

            print(
                f"Peso disponible: "
                f"{vehiculo.peso_disponible()} kg"
            )

            print(
                f"Volumen utilizado: "
                f"{vehiculo.volumen_utilizado():.2f} m3"
            )

            print("\nRuta:")

            print(" -> ".join(ruta))

            print(
                f"\nDistancia total: "
                f"{distancia} km"
            )

    if paquetes_no_asignados:

        print("\n####################################")
        print("PAQUETES NO ASIGNADOS")
        print("///////////////////////////////////////")

        for paquete in paquetes_no_asignados:

            print(
                f"{paquete.codigo} | "
                f"{paquete.peso} kg | "
                f"{paquete.destino}"
            )

    else:

        print("\nTodos los paquetes fueron asignados.")