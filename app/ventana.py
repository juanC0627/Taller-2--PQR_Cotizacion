class Ventana:
    def __init__(self, estilo, ancho, alto, num_naves):
        self.estilo = estilo
        self.ancho = ancho
        self.alto = alto
        self.num_naves = num_naves

    def calcular_tamaños_naves(self):
        nave_ancho = self.ancho / self.num_naves
        return nave_ancho, self.alto

    def __str__(self):
        return f"Ventana estilo {self.estilo}, {self.ancho}x{self.alto}cm, {self.num_naves} naves"