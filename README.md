# Análisis de Ventas - TP Organización Empresarial

**Universidad Tecnológica Nacional - Tecnicatura Universitaria en Programación (TUP)**  
**Modalidad a Distancia - Año Lectivo 2026**  
**Cátedra:** Organización Empresarial

## Integrantes
- Josias Avram

## Escenario elegido
**Escenario B – Análisis de Ventas de una Pequeña Empresa**

Este proyecto analiza datos simulados de ventas comerciales para generar
indicadores básicos que permitan interpretar el desempeño de la empresa.

## Estructura del repositorio

\`\`\`
tup-analisis-ventas-2026/
├── datos/              # Dataset CSV de ventas
├── scripts/            # Script de análisis en Python
├── resultados/         # Gráficos y salidas generadas
├── README.md           # Este archivo
└── .gitignore          # Archivos excluidos del versionado
\`\`\`

## Dataset utilizado
Dataset simulado de ventas comerciales con registros diarios.
Columnas principales: id, sales_date, sales_amount.

## Indicadores calculados
- Ventas totales del período.
- Promedio de ventas diarias.
- Ventas agrupadas por mes.
- Gráfico de evolución mensual.

## Cómo ejecutar
1. Abrir el archivo \`scripts/analisis_ventas.py\` en Google Colab.
2. Asegurarse de que el dataset esté en \`datos/ventas.csv\`.
3. Ejecutar el script. Los resultados se guardan en \`resultados/\`.

## Gestión del proyecto
- **Planificación:** Jira (tablero Kanban con estados Por hacer → En curso → En revisión → En Test → Finalizado).
- **Control de versiones:** Git + GitHub.
- **Trazabilidad:** cada commit referencia el ID de la tarea de Jira correspondiente (OE-5, OE-6, OE-7) según el mandato de trazabilidad establecido en la consigna.
