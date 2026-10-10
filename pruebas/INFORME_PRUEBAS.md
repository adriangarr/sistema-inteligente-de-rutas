# Documento de pruebas

## Casos definidos
1. **Origen igual a destino:** al buscar Centro → Centro, debe devolver `['Centro']`.
2. **Ruta conectada:** Portal Norte → Centro debe devolver un camino cuyo primer elemento sea Portal Norte y último elemento Centro, sin repetir estaciones.
3. **Estación inválida:** una estación no registrada debe devolver `None` sin producir un error.
4. **Entrenamiento del modelo:** el modelo debe entrenarse con el CSV y producir una métrica entre 0 y 1.
5. **Predicción válida:** el modelo debe predecir una de las dos etiquetas permitidas y entregar un camino entre Calle 72 y Centro.

## Ejecución
Desde la carpeta raíz:
```bash
python -m unittest discover -s pruebas -v
```

## Registro de resultados
Completar después de ejecutar las pruebas en el equipo de entrega:
- Fecha y versión de Python:
- Comando ejecutado:
- Pruebas aprobadas / fallidas:
- Observaciones:
- Exactitud del modelo observada:

No reemplazar resultados reales por valores supuestos. La exactitud puede variar si se modifica el dataset, la semilla o los parámetros.
