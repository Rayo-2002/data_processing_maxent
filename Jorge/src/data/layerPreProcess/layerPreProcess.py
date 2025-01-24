import os
import rasterio
from rasterio.enums import Resampling

from .epsg_verify import epsg_verify
from __special__ import data_path
data_folder = os.path.join(data_path, "layerPreProcess")


def layerPreprocess():
    folder_name = "wc2.1_10m_bio_tif"
    folder_path = os.path.join(data_folder, folder_name)

    epsg_flag = epsg_verify(folder_name)

    if epsg_flag:
        output_directory = os.path.join(data_folder, "wc2.1_10m_bio_asc")
        if not os.path.exists(output_directory):
            os.makedirs(output_directory)


        # Listar todos los archivos .tif en el directorio
        tif_files = [f for f in os.listdir(folder_path) if f.endswith(".tif")]

        # Procesar cada archivo .tif
        for f in tif_files:
            input_path = os.path.join(folder_path, f)
            output_path = os.path.join(output_directory, f.replace(".tif", ".asc"))

            # Leer el archivo raster
            with rasterio.open(input_path) as src:
                # Calcular el nuevo tamaño (factor de agregación 2x2)
                new_width = src.width // 2
                new_height = src.height // 2
                data = src.read(
                    out_shape=(
                        src.count,  # Número de bandas
                        new_height,
                        new_width
                    ),
                    resampling=Resampling.average  # Resampling promedio
                )

                # Ajustar los metadatos
                transform = src.transform * src.transform.scale(
                    (src.width / new_width),  # Escalar la resolución en X
                    (src.height / new_height)  # Escalar la resolución en Y
                )
                new_meta = src.meta.copy()
                new_meta.update({
                    "driver": "AAIGrid",  # Formato ASCII
                    "height": new_height,
                    "width": new_width,
                    "transform": transform
                })

                # Guardar el raster en formato .asc
                with rasterio.open(output_path, "w", **new_meta) as dest:
                    dest.write(data)

        print("Procesamiento completado. Archivos .asc guardados en:", output_directory)
    else:
        print("Error: No se pudo realizar el procesamiento debido a que no todos los archivos .tif tienen el sistema de"
              " coordenadas EPSG:4326")


if __name__ == "__main__":
    layerPreprocess()
