import csv
from pathlib import Path


def leer_actividades(ruta_archivo: Path):
    """Lee el archivo CSV de actividades y muestra su contenido formateado por pantalla."""
    if not ruta_archivo.exists():
        print(f"Error: No se encontró el archivo en {ruta_archivo}")
        return

    with open(ruta_archivo, mode="r", encoding="utf-8") as archivo:
        lector_csv = csv.reader(archivo)
        
        # Leemos la cabecera
        cabecera = next(lector_csv, None)
        if cabecera is None:
            print("El archivo CSV está vacío.")
            return

        # Anchos de columna para formatear la salida en tabla
        anchos = [6, 20, 15, 15, 12]
        formato_fila = "{:<6} {:<20} {:<15} {:<15} {:<12}"

        print("=" * 70)
        print(formato_fila.format(*cabecera))
        print("=" * 70)

        for fila in lector_csv:
            if fila:  # Omitir líneas vacías si las hubiera
                print(formato_fila.format(*fila))
        
        print("=" * 70)


if __name__ == "__main__":
    # Resuelve la ruta relativa al directorio donde se encuentra este script
    directorio_base = Path(__file__).resolve().parent
    ruta_csv = directorio_base / "Datos" / "actividades.csv"

    leer_actividades(ruta_csv)
