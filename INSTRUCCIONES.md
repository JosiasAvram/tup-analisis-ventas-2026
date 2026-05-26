# Instrucciones de Uso

## Requisitos previos
- Python 3.8 o superior instalado.
- Git instalado (para clonar el repositorio).
- Acceso a internet (solo para clonar; el script funciona offline).

## Instalacion

### Opcion 1: Google Colab (recomendado)
1. Abrir Google Colab en https://colab.research.google.com
2. Crear un cuaderno nuevo.
3. Clonar el repositorio con el comando git clone.
4. Ejecutar el script con: python scripts/analisis_ventas.py

### Opcion 2: Entorno local
1. Clonar el repositorio con git clone.
2. Instalar dependencias si no se tiene matplotlib: pip install matplotlib
3. Ejecutar: python scripts/analisis_ventas.py

## Estructura de archivos generados
Despues de ejecutar el script, se crean automaticamente:

- resultados/ventas_por_mes.png : grafico de barras con la evolucion mensual.
- resultados/resumen_analisis.txt : texto con los indicadores calculados.

## Solucion de problemas comunes

### Error: FileNotFoundError datos/ventas.csv
- Causa: se esta ejecutando el script desde otra carpeta.
- Solucion: ejecutar siempre desde la raiz del proyecto.

### Error: ModuleNotFoundError matplotlib
- Causa: matplotlib no esta instalado.
- Solucion: pip install matplotlib

## Contacto
Para consultas sobre este TP, contactar a traves del repositorio de GitHub.
