import csv
import pathlib

def leer_csv_login(ruta_archivo):
    ruta = pathlib.Path(__file__).parent.parent / ruta_archivo
    datos = []
    with ruta.open(newline='', encoding="utf-8") as archivo:
        lector = csv.DictReader(archivo)
        for fila in lector:
            debe_funcionar = fila["debe_funcionar"].lower() == "true"
            datos.append((fila["usuario"], fila["password"], debe_funcionar))
    return datos

