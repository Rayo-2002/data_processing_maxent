from data.azorella.azorellaPreProcess import azorellaPreProcess
import pandas as pd
import os
from __special__ import data_path


if __name__ == "__main__":
    name = "datos_azorella"
    azorellaPreProcess(name)

    processed_df = pd.read_csv(os.path.join(data_path, name, "_processed.csv"))
    print(processed_df.columns)
