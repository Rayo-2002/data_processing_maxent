import os
import shutil
import subprocess


from __special__ import data_path


def maxent():
    # Rutas a los archivos y directorios
    java_path = shutil.which("java")  # O la ruta completa al ejecutable de Java
    maxent_jar = os.path.join(os.path.dirname(data_path), "maxent.jar")
    presence_data = os.path.join(data_path, "azorella", "datos_azorella_processed.csv")
    env_layers_dir = os.path.join(data_path, "layerPreProcess", "wc2.1_10m_bio_asc")
    output_directory = os.path.join(data_path, "results")
    if not os.path.exists(output_directory):
        os.makedirs(output_directory)

    # Comando para ejecutar MaxEnt
    comando = [

        java_path, "-mx512m",
        "-jar", maxent_jar,
        "environmentallayers=" + env_layers_dir,
        "samplesfile=" + presence_data,
        "outputdirectory=" + output_directory,
        "autorun",
        "randomseed",
        "threads=2",
        "responsecurves",
        "jackknife",
        "plots=true"

    ]
    print(comando)

    # Ejecutar el comando
    try:
        subprocess.run(comando, check=True)
        print("MaxEnt ejecutado correctamente.")
    except subprocess.CalledProcessError as e:
        print(f"Error al ejecutar MaxEnt: {e}")


if __name__ == "__main__":
    maxent()

