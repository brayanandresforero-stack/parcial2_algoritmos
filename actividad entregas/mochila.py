def mochila_01(paquetes, capacidad):
    """
    Problema de la mochila 0/1.

    Cada paquete puede:
    - Ser seleccionado.
    - No ser seleccionado.

    capacidad = peso máximo del vehículo.

    El algoritmo intenta obtener la mayor prioridad
    sin superar el peso máximo.
    """

    cantidad = len(paquetes)

    # Tabla de programación dinámica.
    #
    # filas = paquetes
    # columnas = capacidad de peso
    #
    # dp[i][peso] representa la mayor prioridad
    # utilizando los primeros i paquetes.
    dp = [
        [0] * (capacidad + 1)
        for _ in range(cantidad + 1)
    ]

    # Construimos la tabla.
    for i in range(1, cantidad + 1):

        paquete = paquetes[i - 1]

        peso = paquete.peso
        prioridad = paquete.prioridad

        for peso_actual in range(capacidad + 1):

            # Opción 1:
            # No llevar el paquete.
            dp[i][peso_actual] = dp[i - 1][peso_actual]

            # Opción 2:
            # Llevar el paquete si cabe.
            if peso <= peso_actual:

                valor_con_paquete = (
                    dp[i - 1][peso_actual - peso]
                    + prioridad
                )

                # Elegimos la mejor opción.
                dp[i][peso_actual] = max(
                    dp[i][peso_actual],
                    valor_con_paquete
                )

    # Ahora reconstruimos los paquetes seleccionados.
    seleccionados = []

    peso_actual = capacidad

    for i in range(cantidad, 0, -1):

        # Si el valor cambió respecto a la fila anterior,
        # significa que el paquete fue seleccionado.
        if dp[i][peso_actual] != dp[i - 1][peso_actual]:

            paquete = paquetes[i - 1]

            seleccionados.append(paquete)

            peso_actual -= paquete.peso

    # Como los encontramos de atrás hacia adelante,
    # invertimos la lista.
    seleccionados.reverse()

    return seleccionados