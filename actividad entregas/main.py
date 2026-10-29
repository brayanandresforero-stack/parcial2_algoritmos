from paquete import Paquete
from vehiculo import Vehiculo
from grafo import crear_grafo
from optimizador import ejecutar_optimizacion

# DATOS INICIALES
vehiculos = [

    Vehiculo(
        "C1",
        "Camion",
        300,
        8
    ),

    Vehiculo(
        "C2",
        "Camion",
        500,
        12
    ),

    Vehiculo(
        "M1",
        "Moto",
        25,
        0.15
    ),

    Vehiculo(
        "M2",
        "Moto",
        30,
        0.20
    )
]


# Cada paquete representa una entrega de mercancia.
# El campo tipo indica que clase de mercancia transporta.

paquetes = [

    Paquete(
        "P1",
        80,
        1.0,
        0.8,
        0.7,
        "Centro",
        "Electronico",
        8
    ),

    Paquete(
        "P2",
        50,
        0.5,
        0.5,
        0.5,
        "Jordan",
        "Alimentos",
        5
    ),

    Paquete(
        "P3",
        120,
        1.2,
        0.8,
        0.8,
        "Picalena",
        "Mueble",
        10
    ),

    Paquete(
        "P4",
        40,
        0.5,
        0.4,
        0.4,
        "Cadiz",
        "Ropa",
        4
    ),

    Paquete(
        "P5",
        30,
        0.4,
        0.4,
        0.3,
        "La Pola",
        "Documentos",
        3
    ),

    Paquete(
        "P6",
        70,
        0.8,
        0.7,
        0.6,
        "Ambala",
        "Electronico",
        7
    ),

    Paquete(
        "P7",
        15,
        0.4,
        0.3,
        0.2,
        "El Salado",
        "Documento",
        2
    ),

    Paquete(
        "P8",
        20,
        0.4,
        0.4,
        0.15,
        "Centro",
        "Ropa",
        3
    ),

    Paquete(
        "P9",
        10,
        0.3,
        0.2,
        0.2,
        "Jordan",
        "Documento",
        2
    )
]


# Crear el grafo de ubicaciones y distancias.
grafo = crear_grafo()

# FUNCIONES DEL MENU

def mostrar_paquetes():

    print("\n++++++++++++++++++++++++++++++++++++++")
    print("          LISTA DE ENTREGAS")
    print("++++++++++++++++++++++++++++++++++++++")

    for paquete in paquetes:

        print(
            f"{paquete.codigo} | "
            f"{paquete.peso} kg | "
            f"{paquete.destino} | "
            f"Prioridad: {paquete.prioridad}"
        )


def consultar_mercancias():
    """
    Consulta la mercancia registrada en cada paquete.
    Esta funcion solamente muestra informacion.
    No modifica los paquetes ni la optimizacion.
    """

    print("\n++++++++++++++++++++++++++++++++++++++")
    print("       MERCANCIAS POR PAQUETE")
    print("++++++++++++++++++++++++++++++++++++++")

    for paquete in paquetes:

        print(f"\nPaquete: {paquete.codigo}")
        print(f"Mercancia: {paquete.tipo}")
        print(f"Peso: {paquete.peso} kg")

        print(
            f"Dimensiones: {paquete.alto} x "
            f"{paquete.ancho} x "
            f"{paquete.profundidad} m"
        )

        print(f"Volumen: {paquete.calcular_volumen():.2f} m3")
        print(f"Destino: {paquete.destino}")
        print(f"Prioridad: {paquete.prioridad}")

    print("\nConsulta finalizada.")


def mostrar_vehiculos():

    print("\n++++++++++++++++++++++++++++++++++++++")
    print("          LISTA DE VEHICULOS")
    print("++++++++++++++++++++++++++++++++++++++")

    for vehiculo in vehiculos:

        print(
            f"{vehiculo.codigo} | "
            f"{vehiculo.tipo} | "
            f"{vehiculo.capacidad_peso} kg | "
            f"{vehiculo.capacidad_volumen} m3"
        )


def registrar_vehiculo():

    print("\n++++++++++++++++++++++++++++++++++++++")
    print("       REGISTRAR VEHICULO")
    print("++++++++++++++++++++++++++++++++++++++")

    codigo = input("Codigo del vehiculo: ")

    tipo = input("Tipo (Camion/Moto): ")

    capacidad_peso = int(
        input("Capacidad de peso en kg: ")
    )

    capacidad_volumen = float(
        input("Capacidad de volumen en m3: ")
    )

    nuevo = Vehiculo(
        codigo,
        tipo,
        capacidad_peso,
        capacidad_volumen
    )

    vehiculos.append(nuevo)

    print("\nVehiculo registrado correctamente.")


def registrar_paquete():

    print("\n++++++++++++++++++++++++++++++++++++++")
    print("        REGISTRAR ENTREGA")
    print("++++++++++++++++++++++++++++++++++++")

    codigo = input("Codigo de la entrega: ")

    peso = int(
        input("Peso en kg: ")
    )

    alto = float(
        input("Alto en metros: ")
    )

    ancho = float(
        input("Ancho en metros: ")
    )

    profundidad = float(
        input("Profundidad en metros: ")
    )

    destino = input("Destino: ")

    tipo = input("Tipo de mercancia: ")

    prioridad = int(
        input("Prioridad de 1 a 10: ")
    )

    nuevo = Paquete(
        codigo,
        peso,
        alto,
        ancho,
        profundidad,
        destino,
        tipo,
        prioridad
    )

    paquetes.append(nuevo)

    print("\nEntrega registrada correctamente.")


def mostrar_grafo():

    print("\n++++++++++++++++++++++++++++++++++++++")
    print("          GRAFO DE RUTAS")
    print("++++++++++++++++++++++++++++++++++++++")

    for origen, conexiones in grafo.items():

        print(f"\n{origen}:")

        for destino, distancia in conexiones:

            print(
                f"  -> {destino}: {distancia} km"
            )

# MENU PRINCIPAL
def menu():

    while True:

        print("\n")
        print("++++++++++++++++++++++++++++++++++++++")
        print(" SISTEMA DE OPTIMIZACION DE TRANSPORTE")
        print("++++++++++++++++++++++++++++++++++++++")

        print("1. Mostrar entregas")
        print("2. Mostrar vehiculos")
        print("3. Registrar entrega")
        print("4. Registrar vehiculo")
        print("5. Mostrar grafo")
        print("6. Ejecutar optimizacion")
        print("7. Consultar mercancias de los paquetes")
        print("0. Salir")

        opcion = input("\nSeleccione una opcion: ")

        if opcion == "1":

            mostrar_paquetes()

        elif opcion == "2":

            mostrar_vehiculos()

        elif opcion == "3":

            registrar_paquete()

        elif opcion == "4":

            registrar_vehiculo()

        elif opcion == "5":

            mostrar_grafo()

        elif opcion == "6":

            # Limpiar asignaciones anteriores para evitar
            # duplicar paquetes al optimizar nuevamente.

            for vehiculo in vehiculos:
                vehiculo.paquetes = []

            ejecutar_optimizacion(
                vehiculos,
                paquetes,
                grafo
            )

        elif opcion == "7":

            # Consultar la mercancia de cada paquete.
            consultar_mercancias()

        elif opcion == "0":

            print("\nPrograma finalizado.")
            break

        else:

            print("\nOpcion no valida.")


# Iniciar el programa.
if __name__ == "__main__":
    menu()
