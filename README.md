# Análisis de Ventas - TP Organización Empresarial

**Universidad Tecnológica Nacional - Tecnicatura Universitaria en Programación (TUP)**  
**Modalidad a Distancia - Año Lectivo 2026**  
**Cátedra:** Organización Empresarial

## Integrantes
- Josias Avram

## Escenario elegido
**Escenario B – Análisis de Ventas de una Pequeña Empresa**

Este proyecto analiza datos simulados de ventas comerciales de una ferretería
para generar indicadores básicos que permitan interpretar el desempeño anual.

## Estructura del repositorio

\`\`\`
tup-analisis-ventas-2026/
├── datos/
│   └── ventas.csv              # Dataset simulado (2725 registros, año 2025)
├── scripts/
│   └── analisis_ventas.py      # Script principal de análisis
├── resultados/
│   ├── ventas_por_mes.png      # Gráfico de evolución mensual
│   └── resumen_analisis.txt    # Resumen textual de indicadores
├── README.md
└── .gitignore
\`\`\`

## Dataset utilizado
Dataset generado programáticamente que simula las ventas diarias de una
ferretería durante el año 2025. Incluye 10 productos típicos del rubro.

**Columnas:**
- `id`: identificador único de la venta
- `sales_date`: fecha de la venta (formato YYYY-MM-DD)
- `producto`: nombre del producto vendido
- `cantidad`: unidades vendidas
- `precio_unitario`: precio base del producto
- `sales_amount`: monto total de la venta (con variación de precio)

## Indicadores calculados
El script `analisis_ventas.py` produce los siguientes indicadores:

1. **Ventas totales del período:** suma de todas las ventas del año.
2. **Ranking de productos:** ordena los productos por unidades vendidas.
3. **Ventas por mes:** agrupación temporal para detectar estacionalidad.
4. **Promedio mensual:** facturación promedio por mes.
5. **Gráfico de barras:** visualiza la evolución mensual de las ventas.

## Cómo ejecutar
1. Clonar el repositorio:
   \`\`\`bash
   git clone https://github.com/JosiasAvram/tup-analisis-ventas-2026.git
   cd tup-analisis-ventas-2026
   \`\`\`
2. Ejecutar el script desde la raíz del proyecto:
   \`\`\`bash
   python scripts/analisis_ventas.py
   \`\`\`
3. Los resultados se generan en la carpeta \`/resultados/\`.

## Requisitos
- Python 3.8 o superior.
- Librería `matplotlib` (incluida por defecto en Google Colab).

## Gestión del proyecto
- **Planificación:** Jira (tablero Kanban con estados Por hacer → En curso → En revisión → En Test → Finalizado).
- **Control de versiones:** Git + GitHub.
- **Flujo de trabajo:** rama principal `main` + rama de desarrollo `feature/desarrollo-analisis` integrada vía Pull Request con revisión por pares.
- **Trazabilidad:** cada commit referencia el ID de la tarea de Jira correspondiente (OE-5, OE-6, OE-7) según el mandato de trazabilidad establecido en la consigna.

## Roles del equipo (Modelo Hugo-Paco-Luis)
- **P1 (Hugo) - OE-5:** Líder y Organizador. Inicialización del repositorio, estructura de carpetas y documentación base.
- **P2 (Paco) - OE-6:** Desarrollador Técnico. Lógica del script, generación del dataset y análisis estadístico.
- **P3 (Luis) - OE-7:** Revisor y QA. Peer Review, mejora de documentación y gestión del Pull Request.
