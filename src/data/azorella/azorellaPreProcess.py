import pandas as pd
import os
from __special__ import data_path

data_path = os.path.join(data_path, "azorella")


def azorellaPreProcess(file_name: str):
    """
    Takes the name of a file of gbif data and creates a new df with the species, latitude and longitude columns.
    :param file_name: Name of the file to preprocess
    """
    file_path = os.path.join(data_path, f"{file_name}.csv")
    df = pd.read_csv(file_path, sep='\t')
    df = df[df['decimalLatitude'].notna()]

    species = df["species"]
    latitudes = df["decimalLatitude"]
    longitudes = df["decimalLongitude"]
    new_df = pd.DataFrame({"species": species, "latitude": latitudes, "longitude": longitudes})

    new_df.to_csv(os.path.join(data_path, f"{file_name}_processed.csv"), index=False)


if __name__ == "__main__":
    name = "datos_azorella"
    azorellaPreProcess(name)

    processed_df = pd.read_csv(os.path.join(data_path, name, "_processed.csv"))
    print(processed_df.columns)

