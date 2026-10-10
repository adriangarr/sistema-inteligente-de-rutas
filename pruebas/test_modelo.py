import unittest
from pathlib import Path
import pandas as pd
from modelo_transporte import buscar_ruta, recomendar_ruta, entrenar_modelo, RUTAS

class TestSistemaRutas(unittest.TestCase):
    def test_ruta_misma_estacion(self):
        self.assertEqual(buscar_ruta("Centro", "Centro"), ["Centro"])

    def test_ruta_conectada(self):
        ruta = buscar_ruta("Portal Norte", "Centro")
        self.assertIsNotNone(ruta)
        self.assertEqual(ruta[0], "Portal Norte")
        self.assertEqual(ruta[-1], "Centro")
        self.assertEqual(len(ruta), len(set(ruta)))

    def test_estacion_invalida(self):
        self.assertIsNone(buscar_ruta("Estacion inventada", "Centro"))

    def test_dos_alternativas_modelo(self):
        proyecto = Path(__file__).resolve().parents[1]
        modelo, precision = entrenar_modelo(proyecto / "datos" / "datos_transporte_simulados.csv")
        self.assertGreaterEqual(precision, 0.0)
        self.assertLessEqual(precision, 1.0)
        etiqueta, camino = recomendar_ruta(modelo, "Soleado", "Pesado", "Mañana", "Alta")
        self.assertIn(etiqueta, {"Via Calle 63", "Via Museo Nacional"})
        self.assertEqual(camino[0], "Calle 72")
        self.assertEqual(camino[-1], "Centro")

if __name__ == "__main__":
    unittest.main()
