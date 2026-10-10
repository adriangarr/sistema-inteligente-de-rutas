# Mapa conceptual — Sistema Inteligente de Rutas

Copia este bloque en un visor compatible con Mermaid (por ejemplo, Mermaid Live Editor) para visualizarlo, o consérvalo como mapa conceptual dentro del repositorio.

```mermaid
flowchart TD
    A["Sistema Inteligente de Rutas"] --> B["Grafo de estaciones"]
    A --> C["Aprendizaje supervisado"]
    B --> D["Estaciones y conexiones"]
    D --> E["Búsqueda recursiva"]
    E --> F["Camino válido entre origen y destino"]
    C --> G["Dataset simulado etiquetado"]
    G --> H["Variables: clima, tráfico, hora y demanda"]
    H --> I["Preparación: OneHotEncoder"]
    I --> J["Entrenamiento: árbol de decisión"]
    J --> K["Evaluación con datos de prueba"]
    K --> L["Predicción de alternativa"]
    L --> M["Vía Calle 63"]
    L --> N["Vía Museo Nacional"]
    F --> O["Sistema integrado"]
    M --> O
    N --> O
    O --> P["Limitación: datos sintéticos, no oficiales"]
```

## Explicación
El grafo representa las estaciones y sus conexiones. La búsqueda recursiva encuentra un camino entre estaciones. Para el tramo Calle 72 → Centro, el clasificador supervisado aprende de ejemplos etiquetados y recomienda una de dos alternativas usando las condiciones del viaje. Ambos componentes se integran en un solo programa.
