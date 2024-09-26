
# PQR_Cotizacion

**Presentado por:** Juan Camilo Diaz Erazo  
**Presentado a:** Diego Marin  
**Curso:** Lenguaje de Programacion Avanzado 1

Sistema de cotización de ventanas para PQR, diseñado para automatizar cálculos y mejorar la eficiencia.



## Listado de Requerimientos

**Sistema de Cotización para Ventanas PQR:**

 Estilos de Ventanas:

O, XO, OXXO, OXO (otros estilos deben ser aprobados por la gerencia).
Factores de Cálculo de Precio:

Tamaño de la ventana: Ancho x alto.
Tipo de aluminio (acabado): Pulido, Lacado Brillante, Lacado Mate, Anodizado.
Tipo de vidrio: Transparente, Bronce, Azul (con opción de esmerilado).
Cálculo del aluminio: Precio por cm lineal, tomando en cuenta esquinas y perfiles.
Cálculo del vidrio: Precio por cm², considerando que el vidrio es 1.5 cm más pequeño por lado.
Costos adicionales: Chapas, esquinas, descuento del 10% para cantidades mayores a 100.
Características del Sistema:

Registro de tipos de ventanas y materiales.
Cálculo automático de costos basados en los parámetros ingresados.
Aplicación de descuentos si corresponde.
Soporte para consulta y modificación de cotizaciones.
Diagrama de Clases
Para diseñar las clases:

Ventana: Atributos como ancho, alto, estilo, número de naves, etc.
Aluminio: Tipo de acabado, precio por metro lineal.
Vidrio: Tipo de vidrio, precio por cm², opción esmerilado.
Cotización: Descuentos aplicados, total de la cotización.


## Tech Stack

**Language:** Pyton

Base de datos para guardar cotizaciones.



