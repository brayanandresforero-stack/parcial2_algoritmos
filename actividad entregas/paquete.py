class Paquete:
# Representa un paquete que debe ser transportado.

    def __init__(self, codigo, peso, alto, ancho, profundidad,
                destino, tipo, prioridad):

        self.codigo = codigo
        self.peso = peso
        self.alto = alto
        self.ancho = ancho
        self.profundidad = profundidad
        self.destino = destino
        self.tipo = tipo
        self.prioridad = prioridad

    def calcular_volumen(self):
        """
        Calcula el volumen del paquete.
        Formula:
        volumen = alto * ancho * profundidad
        """

        return self.alto * self.ancho * self.profundidad

    def mostrar(self):
        #Muestra la información del paquete.
        print(f"Codigo: {self.codigo}")
        print(f"Peso: {self.peso} kg")
        print(f"Dimensiones: {self.alto} x {self.ancho} x {self.profundidad} m")
        print(f"Volumen: {self.calcular_volumen():.2f} m3")
        print(f"Destino: {self.destino}")
        print(f"Tipo: {self.tipo}")
        print(f"Prioridad: {self.prioridad}")