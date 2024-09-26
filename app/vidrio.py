class Vidrio:
    precios = {
        "transparente": 8.25,
        "bronce": 9.15,
        "azul": 12.75,
    }

    def __init__(self, tipo_vidrio, esmerilado=False):
        self.tipo_vidrio = tipo_vidrio
        self.esmerilado = esmerilado

    def calcular_precio(self, area_cm2):
        precio = area_cm2 * self.precios.get(self.tipo_vidrio)
        if self.esmerilado:
            precio += area_cm2 * 5.20  # Costo adicional por esmerilado
        return precio

    def __str__(self):
        esmerilado_str = "con esmerilado" if self.esmerilado else "sin esmerilado"
        return f"Vidrio {self.tipo_vidrio}, {esmerilado_str}"