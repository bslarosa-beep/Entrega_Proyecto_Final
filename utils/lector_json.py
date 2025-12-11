import json
from pathlib import Path

def leer_json_productos(ruta_relativa):
    # Ruta absoluta basada en la ubicación de este script
    base_dir = Path(__file__).resolve().parent.parent  # sube hasta PreEntrega_BarbaraLaRosa_Final
    ruta = base_dir / ruta_relativa

    with ruta.open("r", encoding="utf-8") as archivo:
        data = json.load(archivo)
    return [producto["nombre"] for producto in data]