# Guion sugerido para el video (máximo 10 minutos)

**0:00–0:45 — Presentación**  
“Somos el equipo de la actividad 5. Nuestro proyecto se llama Sistema Inteligente de Rutas. En la entrega anterior desarrollamos un grafo de estaciones y una búsqueda recursiva. Ahora integramos aprendizaje supervisado.”

**0:45–2:00 — Grafo y búsqueda**  
Mostrar `RUTAS`, `ESTACIONES` y `buscar_ruta`. Explicar que cada estación está conectada con sus vecinas y que la recursividad explora caminos sin repetir estaciones.

**2:00–3:30 — Dataset**  
Abrir `datos/datos_transporte_simulados.csv`. Explicar las columnas y decir explícitamente que los 600 registros son simulados para fines académicos, no datos oficiales.

**3:30–5:30 — Modelo**  
Mostrar `train_test_split`, `OneHotEncoder`, `DecisionTreeClassifier` y `Pipeline`. Explicar que se separan datos de entrenamiento y prueba, se codifican categorías y se entrena el árbol.

**5:30–7:00 — Ejecución y evaluación**  
Ejecutar `python modelo_transporte.py` o la instrucción de evaluación. Mostrar la exactitud y el reporte de clasificación reales que aparezcan al ejecutar. No leer cifras inventadas.

**7:00–8:30 — Demostración**  
Elegir origen D (Calle 72) y destino J (Centro). Ingresar clima, tráfico, hora y demanda con valores válidos. Mostrar la alternativa predicha y explicar que se trata de una recomendación académica basada en datos simulados.

**8:30–9:30 — Pruebas y limitaciones**  
Ejecutar `python -m unittest discover -s pruebas -v`. Explicar que la evaluación con datos sintéticos no demuestra rendimiento en transporte real.

**9:30–10:00 — Cierre**  
Mencionar próximos pasos: buscar datos confiables, medir tiempos reales y validar el modelo. Cada integrante debe participar; distribuyan los segmentos antes de grabar.
