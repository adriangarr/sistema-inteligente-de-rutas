"""
Sistema Inteligente de Rutas
Integra el grafo recursivo de la entrega anterior con un clasificador supervisado.
El dataset es SIMULADO con fines académicos; no representa datos oficiales.
Requisitos: pandas, scikit-learn
Instalación: python -m pip install -r requirements.txt
Ejecución: python modelo_transporte.py
"""
from pathlib import Path
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.compose import ColumnTransformer
from sklearn.preprocessing import OneHotEncoder
from sklearn.tree import DecisionTreeClassifier, export_text
from sklearn.pipeline import Pipeline
from sklearn.metrics import accuracy_score, classification_report

RUTAS = {
    "Portal Norte": ["Calle 100"],
    "Calle 100": ["Portal Norte", "Héroes"],
    "Héroes": ["Calle 100", "Calle 72"],
    "Calle 72": ["Héroes", "Calle 63", "Museo Nacional"],
    "Calle 63": ["Calle 72", "Calle 57", "Centro"],
    "Calle 57": ["Calle 63", "Calle 45"],
    "Calle 45": ["Calle 57", "Marly"],
    "Marly": ["Calle 45", "Museo Nacional"],
    "Museo Nacional": ["Marly", "Centro"],
    "Centro": ["Museo Nacional", "Avenida El Dorado", "Calle 63"],
    "Avenida El Dorado": ["Centro"]
}

ESTACIONES = {
    "A": "Portal Norte", "B": "Calle 100", "C": "Héroes",
    "D": "Calle 72", "E": "Calle 63", "F": "Calle 57",
    "G": "Calle 45", "H": "Marly", "I": "Museo Nacional",
    "J": "Centro", "K": "Avenida El Dorado"
}

def buscar_ruta(origen, destino, ruta=None):
    """Busca un camino válido sin repetir estaciones; conserva la lógica recursiva original."""
    if origen not in RUTAS or destino not in RUTAS:
        return None
    ruta = (ruta or []) + [origen]
    if origen == destino:
        return ruta
    for estacion in RUTAS[origen]:
        if estacion not in ruta:
            nueva_ruta = buscar_ruta(estacion, destino, ruta)
            if nueva_ruta:
                return nueva_ruta
    return None

def entrenar_modelo(ruta_csv="datos/datos_transporte_simulados.csv"):
    """Entrena un árbol de decisión usando los datos simulados."""
    ruta_csv = Path(ruta_csv)
    if not ruta_csv.exists():
        # permite ejecutar desde la carpeta raíz del proyecto o desde este archivo
        ruta_csv = Path(__file__).resolve().parent / "datos" / "datos_transporte_simulados.csv"
    datos = pd.read_csv(ruta_csv)
    columnas = ["Origen", "Destino", "Clima", "Trafico", "Hora", "Demanda"]
    X = datos[columnas]
    y = datos["Ruta_recomendada"]
    categoricas = columnas
    preparador = ColumnTransformer([
        ("categorias", OneHotEncoder(handle_unknown="ignore"), categoricas)
    ])
    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.25, random_state=42, stratify=y
    )
    modelo = Pipeline([
        ("preparacion", preparador),
        ("arbol", DecisionTreeClassifier(max_depth=5, random_state=42))
    ])
    modelo.fit(X_train, y_train)
    predicciones = modelo.predict(X_test)
    precision = accuracy_score(y_test, predicciones)
    print("\n=== EVALUACIÓN DEL MODELO ===")
    print(f"Registros totales: {len(datos)}")
    print(f"Registros de entrenamiento: {len(X_train)}")
    print(f"Registros de prueba: {len(X_test)}")
    print(f"Exactitud (accuracy): {precision:.3f}")
    print(classification_report(y_test, predicciones, zero_division=0))
    print("Reglas aprendidas por el árbol:")
    nombres = modelo.named_steps["preparacion"].get_feature_names_out()
    print(export_text(modelo.named_steps["arbol"], feature_names=list(nombres)))

    # Guardar resultados de evaluación para la documentación
    Path("resultados").mkdir(exist_ok=True)
    with open("resultados/evaluacion.txt", "w", encoding="utf-8") as f:
        f.write(f"Registros totales: {len(datos)}\n")
        f.write(f"Entrenamiento: {len(X_train)}\nPrueba: {len(X_test)}\n")
        f.write(f"Accuracy: {precision:.4f}\n\n")
        f.write(classification_report(y_test, predicciones, zero_division=0))
    return modelo, precision

def recomendar_ruta(modelo, clima, trafico, hora, demanda):
    """Predice una de las dos alternativas para el tramo Calle 72 -> Centro."""
    entrada = pd.DataFrame([{
        "Origen": "Calle 72", "Destino": "Centro",
        "Clima": clima, "Trafico": trafico,
        "Hora": hora, "Demanda": demanda
    }])
    prediccion = modelo.predict(entrada)[0]
    alternativas = {
        "Via Calle 63": ["Calle 72", "Calle 63", "Centro"],
        "Via Museo Nacional": ["Calle 72", "Museo Nacional", "Centro"]
    }
    return prediccion, alternativas[prediccion]

def main():
    print("=" * 52)
    print(" SISTEMA INTELIGENTE DE RUTAS")
    print("=" * 52)
    print("\nEstaciones disponibles:")
    for letra, nombre in ESTACIONES.items():
        print(f"{letra}. {nombre}")
    origen_letra = input("\nLetra de origen: ").strip().upper()
    destino_letra = input("Letra de destino: ").strip().upper()
    if origen_letra not in ESTACIONES or destino_letra not in ESTACIONES:
        print("Error: selecciona letras de estación válidas.")
        return
    origen, destino = ESTACIONES[origen_letra], ESTACIONES[destino_letra]
    ruta = buscar_ruta(origen, destino)
    if not ruta:
        print("No existe una ruta entre las estaciones.")
        return
    print("\nRuta de conectividad encontrada (búsqueda recursiva):")
    print(" -> ".join(ruta))
    print("Número de estaciones:", len(ruta))

    # El clasificador se usa para el tramo donde el grafo tiene dos alternativas.
    if origen == "Calle 72" and destino == "Centro":
        modelo, _ = entrenar_modelo()
        print("\nIngrese condiciones simuladas para comparar las dos alternativas.")
        clima = input("Clima (Soleado/Nublado/Lluvioso): ").strip().capitalize()
        trafico = input("Tráfico (Ligero/Moderado/Pesado): ").strip().capitalize()
        hora = input("Hora (Mañana/Tarde/Noche): ").strip().capitalize()
        demanda = input("Demanda (Baja/Media/Alta): ").strip().capitalize()
        validaciones = {
            "Clima": (clima, {"Soleado", "Nublado", "Lluvioso"}),
            "Tráfico": (trafico, {"Ligero", "Moderado", "Pesado"}),
            "Hora": (hora, {"Mañana", "Tarde", "Noche"}),
            "Demanda": (demanda, {"Baja", "Media", "Alta"})
        }
        invalidos = [k for k, (v, opciones) in validaciones.items() if v not in opciones]
        if invalidos:
            print("Valores no válidos en:", ", ".join(invalidos))
            print("Revisa las opciones indicadas entre paréntesis.")
            return
        prediccion, camino = recomendar_ruta(modelo, clima, trafico, hora, demanda)
        print("\nRecomendación del modelo supervisado:")
        print(prediccion)
        print(" -> ".join(camino))
        print("\nNota: recomendación académica basada en datos simulados, no en tráfico real.")

if __name__ == "__main__":
    main()
