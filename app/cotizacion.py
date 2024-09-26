class Cotizacion:
    def __init__(self, ventana, aluminio, vidrio):
        self.ventana = ventana
        self.aluminio = aluminio
        self.vidrio = vidrio

    def calcular_precio_total(self):
        nave_ancho, nave_alto = self.ventana.calcular_tamanos_naves()
        area_vidrio = (nave_ancho - 1.5) * (nave_alto - 1.5)  # Ajuste del vidrio
        perimetro_nave = 2 * (nave_ancho + nave_alto) - 4  # Restar esquinas

        # Calcular precios
        precio_aluminio = self.aluminio.calcular_precio(perimetro_nave * self.ventana.num_naves)
        precio_vidrio = self.vidrio.calcular_precio(area_vidrio * self.ventana.num_naves)

        # Agregar costos de chapas y esquinas
        costo_chapas = 16200 * (self.ventana.num_naves - 1)
        costo_esquinas = 4310 * 4

        return precio_aluminio + precio_vidrio + costo_chapas + costo_esquinas

    def aplicar_descuento(self, cantidad):
        total = self.calcular_precio_total() * cantidad
        if cantidad > 100:
            total *= 0.9  # Aplicar 10% de descuento
        return total

    def __str__(self):
        return f"Cotización para {self.ventana}\nAluminio: {self.aluminio}\nVidrio: {self.vidrio}\nTotal: {self.calcular_precio_total()}"