import pathlib
import pandas as pd

THIS_DIR = pathlib.Path(__file__).parent
DATA_DIR = THIS_DIR / '..' / 'data'
DATASET_PATHS = {
    "earthquakes": DATA_DIR / 'earthquakes-projected.parq',
    "population_density": DATA_DIR / 'raster' / 'gpw_v4_population_density_rev11_2010_2pt5_min.nc',
    
}


def check_data(file_path=DATASET_PATHS["earthquakes"]):
    """
    Checks if the data file exists and reads it.

    Args:
        file_path (str, optional): The path to the parquet file. Default is '../data/earthquakes-projected.parq'.

    """
    path = pathlib.Path(file_path)
    
    if not path.is_file():
        print(f"Data file does not exist at {file_path}")

    try:
        columns = ['depth', 'id', 'latitude', 'longitude', 'mag', 'place', 'time', 'type']
        data = pd.read_parquet(path, columns=columns, engine='pyarrow')
        data.head()
        print("Data exists and is readable!")       
    except RuntimeError as e:
        print(f"The data cannot be read: {str(e)}")