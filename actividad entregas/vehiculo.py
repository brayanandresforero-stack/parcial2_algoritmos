class Vehiculo:
    #Representa un vehículo de transporte.

    def __init__(self, codigo, tipo, capacidad_peso, capacidad_volumen):
        self.codigo = codigo
        self.tipo = tipo
        self.capacidad_peso = capacidad_peso
        self.capacidad_volumen = capacidad_volumen
        self.paquetes = []

    def peso_utilizado(self):
        #        Suma el peso de todos los paquetes asignados.
        return sum(paquete.peso for paquete in self.paquetes)

    def volumen_utilizado(self):
        # Suma el volumen de todos los paquetes asignados.
        return sum(
            paquete.calcular_volumen()
            for paquete in self.paquetes
        )

    def peso_disponible(self):
        return self.capacidad_peso - self.peso_utilizado()

    def volumen_disponible(self):
        return self.capacidad_volumen - self.volumen_utilizado()

    def agregar_paquete(self, paquete):
        # Agrega un paquete al vehículo.

        self.paquetes.append(paquete)

    def mostrar(self):
        print("\n------------------------------------")
        print(f"Vehiculo: {self.codigo}")
        print(f"Tipo: {self.tipo}")
        print(f"Capacidad de peso: {self.capacidad_peso} kg")
        print(f"Capacidad de volumen: {self.capacidad_volumen} m3")

        print("\nPaquetes asignados:")

        if len(self.paquetes) == 0:
            print("No tiene paquetes.")

        for paquete in self.paquetes:
            print(
                f"- {paquete.codigo} | "
                f"{paquete.peso} kg | "
                f"{paquete.destino}"
            )

        print(f"\nPeso utilizado: {self.peso_utilizado()} kg")
        print(f"Peso disponible: {self.peso_disponible()} kg")

        print(f"Volumen utilizado: {self.volumen_utilizado():.2f} m3")
        print(f"Volumen disponible: {self.volumen_disponible():.2f} m3")