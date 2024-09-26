class Aluminio:
    precios = {
        "pulido": 50700,
        "lacado_brillante": 54200,
        "lacado_mate": 53600,
        "anodizado": 57300
    }

    def __init__(self, tipo_acabado):
        self.tipo_acabado = tipo_acabado

    def calcular_precio(self, cm_lineales):
        return cm_lineales * (self.precios.get(self.tipo_acabado) / 100)

    def __str__(self):
        return f"Aluminio {self.tipo_acabado}, precio por cm lineal: {self.precios.get(self.tipo_acabado)}"