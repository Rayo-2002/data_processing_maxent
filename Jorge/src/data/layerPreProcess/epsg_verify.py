import os
import rasterio

from __special__ import data_path
data_folder = os.path.join(data_path, "layerPreProcess")


def epsg_verify(folder_name: str) -> bool:
    """
    Verifies if all .tif files in the specified directory have the EPSG:4326 coordinate system.

    :param folder_name: Path to the directory containing the "wc2.1_10m_bio_tif" folder with .tif files.
    :return: Returns True if all .tif files have the EPSG:4326 projection; False otherwise.
    """
    directory = os.path.join(data_folder, folder_name)
    flag_val = True

    for root, dirs, files in os.walk(directory):
        for file in files:
            if file.endswith('.tif'):
                ruta_tif = os.path.join(root, file)
                try:
                    with rasterio.open(ruta_tif) as src:
                        if src.crs != rasterio.crs.CRS.from_epsg(4326):
                            print(f"Advertencia: {ruta_tif} no tiene el sistema de coordenadas EPSG:4326")
                            flag_val = False
                except Exception as e:
                    print(f"Error al abrir {ruta_tif}: {e}")
                    flag_val = False

    if flag_val:
        print("Todos los archivos .tif tienen el sistema de coordenadas EPSG:4326")

    return flag_val


if __name__ == "__main__":
    data_path = "wc2.1_10m_bio_tif"
    epsg_verify(data_path)
