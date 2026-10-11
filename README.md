# Sistema Inteligente de Rutas — Actividad 3

Proyecto académico que integra la búsqueda recursiva de rutas de la entrega anterior con un modelo de aprendizaje supervisado (árbol de decisión).

## Alcance y advertencia
El grafo de estaciones se basa en el código compartido en la conversación. El archivo `datos/datos_transporte_simulados.csv` contiene **datos sintéticos** generados para la actividad. No son datos oficiales ni mediciones reales de tráfico. El modelo solo recomienda entre dos alternativas del tramo **Calle 72 → Centro**; la búsqueda recursiva sigue funcionando para los demás pares de estaciones.

## Estructura
- `modelo_transporte.py`: buscador de rutas, entrenamiento, evaluación y recomendación.
- `datos/datos_transporte_simulados.csv`: 600 filas de datos sintéticos.
- `documentacion/descripcion_datos.md`: variables, procedencia y limitaciones.
- `documentacion/mapa_conceptual.md`: mapa conceptual en Mermaid.
- `documentacion/guion_video.md`: guion de video de máximo 10 minutos.
- `pruebas/test_modelo.py`: pruebas automatizadas.
- `pruebas/INFORME_PRUEBAS.md`: guía para registrar resultados.
- `resultados/`: resultados de evaluación de referencia generados al ejecutar el modelo.
- `entrega.pdf`: documento para enlazar el repositorio y el video cuando estén publicados.

## Requisitos y ejecución
Python 3.10 o posterior recomendado.

```bash
python -m pip install -r requirements.txt
python modelo_transporte.py
```

Para evaluar y entrenar sin pasar por el menú interactivo:
```bash
python -c "from modelo_transporte import entrenar_modelo; entrenar_modelo()"
```

## Pruebas
Desde la raíz del proyecto:
```bash
python -m unittest discover -s pruebas -v
```


