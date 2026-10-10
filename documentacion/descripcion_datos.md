# Descripción del dataset

## Objetivo
Entrenar un clasificador supervisado que recomiende una de dos alternativas para el tramo Calle 72 → Centro, incorporando condiciones simuladas de viaje.

## Procedencia
Los 600 registros de `datos_transporte_simulados.csv` fueron generados artificialmente para fines académicos. No se consultaron sensores, GPS, datos operacionales ni fuentes oficiales. Las etiquetas se asignaron mediante una regla explícita de puntuación que simula cómo tráfico, hora, clima y demanda podrían influir en la elección. Se agregó una pequeña proporción de variación para evitar que todas las etiquetas sigan una regla perfectamente determinista.

## Diccionario de variables

| Columna | Tipo | Descripción |
|---|---|---|
| Origen | Categórica | Estación de partida. En este dataset: Calle 72. |
| Destino | Categórica | Estación de llegada. En este dataset: Centro. |
| Clima | Categórica | Soleado, Nublado o Lluvioso. |
| Trafico | Categórica | Ligero, Moderado o Pesado; valor simulado. |
| Hora | Categórica | Mañana, Tarde o Noche. |
| Demanda | Categórica | Baja, Media o Alta; valor simulado. |
| Ruta_recomendada | Etiqueta | Vía Calle 63 o Vía Museo Nacional. |

## Alternativas de recorrido
- Vía Calle 63: Calle 72 → Calle 63 → Centro.
- Vía Museo Nacional: Calle 72 → Museo Nacional → Centro.

Las dos alternativas se encuentran representadas como conexiones del grafo del proyecto. El sistema no mide tiempos de viaje reales; la recomendación refleja únicamente patrones artificiales definidos para la actividad.

## Preparación y aprendizaje
Se separan las variables predictoras (Origen, Destino, Clima, Trafico, Hora, Demanda) de la etiqueta `Ruta_recomendada`. `OneHotEncoder` convierte las categorías a variables numéricas y `DecisionTreeClassifier` aprende patrones. La división de entrenamiento/prueba se realiza con `test_size=0.25` y `random_state=42`.

## Limitaciones y trabajo futuro
- No es una fuente de datos real ni una recomendación para desplazamientos reales.
- El alcance del modelo está limitado al tramo Calle 72 → Centro.
- La exactitud sobre datos sintéticos no demuestra desempeño en el mundo real.
- Para una versión operativa se necesitarían datos confiables de tiempos, incidentes, demanda y estado del servicio, además de validar la calidad y actualidad de esos datos.
