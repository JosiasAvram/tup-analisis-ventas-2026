"""
Análisis de Ventas - Escenario B
TP Organización Empresarial - UTN TUP 2026

Este script procesa el dataset de ventas y genera indicadores básicos
para interpretar el desempeño comercial.
"""

import csv
import os
from collections import defaultdict
from datetime import datetime
import matplotlib.pyplot as plt


# ----------------------------------------------------------------------
# Configuración de rutas
# ----------------------------------------------------------------------
# El por qué de usar rutas relativas: el script debe ser reproducible
# en cualquier entorno (Colab, máquina local, otra computadora del equipo)
# sin necesidad de modificar paths absolutos.
RUTA_DATOS = os.path.join("datos", "ventas.csv")
RUTA_RESULTADOS = "resultados"


# ----------------------------------------------------------------------
# Carga del dataset
# ----------------------------------------------------------------------
# Leemos el CSV línea por línea con csv.DictReader porque permite acceder
# a las columnas por nombre (más legible que por índice) y es parte de la
# librería estándar de Python (no requiere instalar pandas).
ventas = []
with open(RUTA_DATOS, "r", encoding="utf-8") as f:
    lector = csv.DictReader(f)
    for fila in lector:
        # Convertimos los tipos: el CSV guarda todo como string,
        # pero necesitamos números para las operaciones aritméticas
        fila["cantidad"] = int(fila["cantidad"])
        fila["sales_amount"] = float(fila["sales_amount"])
        fila["sales_date"] = datetime.strptime(fila["sales_date"], "%Y-%m-%d")
        ventas.append(fila)

print(f"Registros cargados: {len(ventas)}")


# ----------------------------------------------------------------------
# Indicador 1: Ventas totales
# ----------------------------------------------------------------------
# Sumamos todos los montos (sales_amount) para obtener la facturación total.
total_ventas = 0
for v in ventas:
    total_ventas += v["sales_amount"]

print(f"\nVentas totales del período: ${total_ventas:,.2f}")


# ----------------------------------------------------------------------
# Indicador 2: Producto más vendido (por cantidad de unidades)
# ----------------------------------------------------------------------
# Usamos un diccionario para acumular cantidades por producto.
# defaultdict(int) inicializa cada clave nueva en 0 automáticamente,
# evitando tener que chequear si el producto ya existe en el diccionario.
unidades_por_producto = defaultdict(int)
for v in ventas:
    unidades_por_producto[v["producto"]] += v["cantidad"]

# Ordenamos de mayor a menor para obtener el top
top_productos = sorted(unidades_por_producto.items(),
                       key=lambda x: x[1], reverse=True)

print("\nRanking de productos por unidades vendidas:")
for producto, unidades in top_productos:
    print(f"  {producto}: {unidades} unidades")

producto_estrella = top_productos[0][0]
print(f"\nProducto más vendido: {producto_estrella}")


# ----------------------------------------------------------------------
# Indicador 3: Ventas agrupadas por mes
# ----------------------------------------------------------------------
# Agrupamos por año-mes para ver la evolución temporal.
# Usamos strftime para formatear la fecha como "YYYY-MM", que ordena
# correctamente al ser un string lexicográficamente comparable.
ventas_por_mes = defaultdict(float)
for v in ventas:
    clave_mes = v["sales_date"].strftime("%Y-%m")
    ventas_por_mes[clave_mes] += v["sales_amount"]

# Ordenamos cronológicamente
meses_ordenados = sorted(ventas_por_mes.keys())

print("\nVentas por mes:")
for mes in meses_ordenados:
    print(f"  {mes}: ${ventas_por_mes[mes]:,.2f}")


# ----------------------------------------------------------------------
# Indicador 4: Promedio mensual
# ----------------------------------------------------------------------
promedio_mensual = total_ventas / len(meses_ordenados)
print(f"\nPromedio de ventas mensuales: ${promedio_mensual:,.2f}")


# ----------------------------------------------------------------------
# Visualización: gráfico de evolución de ventas mensuales
# ----------------------------------------------------------------------
# Generamos un gráfico de barras para visualizar la tendencia.
# Lo guardamos en /resultados con savefig() ANTES de show() porque
# show() limpia la figura y rompería el archivo guardado.
montos = [ventas_por_mes[m] for m in meses_ordenados]

plt.figure(figsize=(12, 6))
plt.bar(meses_ordenados, montos, color="steelblue", edgecolor="black")
plt.title("Evolución de ventas mensuales - 2025", fontsize=14)
plt.xlabel("Mes")
plt.ylabel("Ventas totales ($)")
plt.xticks(rotation=45)  # Rotamos las etiquetas para evitar superposición
plt.grid(axis="y", alpha=0.3)
plt.tight_layout()  # Ajusta márgenes para que no se corten las etiquetas

# Guardar el gráfico en /resultados (ruta relativa para reproducibilidad)
ruta_grafico = os.path.join(RUTA_RESULTADOS, "ventas_por_mes.png")
plt.savefig(ruta_grafico, dpi=100)
plt.show()

print(f"\nGráfico guardado en: {ruta_grafico}")


# ----------------------------------------------------------------------
# Exportar resumen de resultados a un archivo de texto
# ----------------------------------------------------------------------
# Guardamos los indicadores en /resultados para que queden documentados
# junto al gráfico, facilitando la trazabilidad del análisis.
ruta_resumen = os.path.join(RUTA_RESULTADOS, "resumen_analisis.txt")
with open(ruta_resumen, "w", encoding="utf-8") as f:
    f.write("RESUMEN DEL ANÁLISIS DE VENTAS\n")
    f.write("=" * 40 + "\n\n")
    f.write(f"Total de registros analizados: {len(ventas)}\n")
    f.write(f"Ventas totales: ${total_ventas:,.2f}\n")
    f.write(f"Producto más vendido: {producto_estrella}\n")
    f.write(f"Promedio mensual: ${promedio_mensual:,.2f}\n\n")
    f.write("Ventas por mes:\n")
    for mes in meses_ordenados:
        f.write(f"  {mes}: ${ventas_por_mes[mes]:,.2f}\n")

print(f"Resumen guardado en: {ruta_resumen}")
print("\nAnálisis completado correctamente.")
