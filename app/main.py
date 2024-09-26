from ventana import Ventana
from aluminio import Aluminio
from vidrio import Vidrio
from cotizacion import Cotizacion

def main():
    # Crear una ventana estilo XO, tamaño 120x90cm, con 2 naves
    ventana = Ventana("XO", 120, 90, 2)

    # Elegir aluminio pulido
    aluminio = Aluminio("pulido")

    # Elegir vidrio transparente con opción esmerilado
    vidrio = Vidrio("transparente", esmerilado=True)

    # Generar la cotización
    cotizacion = Cotizacion(ventana, aluminio, vidrio)
    print(cotizacion)

    # Calcular el precio total para 120 ventanas
    total = cotizacion.aplicar_descuento(120)
    print(f"Total con descuento por 120 ventanas: ${total:.2f}")

if __name__ == "__main__":
    main()