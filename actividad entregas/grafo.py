def crear_grafo():
    """
    Crea el grafo de ubicaciones.

    Cada ubicación es un nodo.
    Cada conexión tiene una distancia en kilómetros.

    Las distancias son ficticias para el ejercicio.
    """

    grafo = {

        "Bodega": [
            ("Centro", 5),
            ("Jordan", 8),
            ("El Salado", 10)
        ],

        "Centro": [
            ("Bodega", 5),
            ("Cadiz", 4),
            ("La Pola", 3),
            ("Picalena", 8)
        ],

        "Jordan": [
            ("Bodega", 8),
            ("Cadiz", 6),
            ("Picalena", 7)
        ],

        "El Salado": [
            ("Bodega", 10),
            ("Ambala", 6)
        ],

        "Cadiz": [
            ("Centro", 4),
            ("Jordan", 6),
            ("La Pola", 2)
        ],

        "La Pola": [
            ("Centro", 3),
            ("Cadiz", 2),
            ("Ambala", 5)
        ],

        "Picalena": [
            ("Centro", 8),
            ("Jordan", 7)
        ],

        "Ambala": [
            ("La Pola", 5),
            ("El Salado", 6)
        ]
    }

    return grafo