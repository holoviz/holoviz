import pathlib
import pandas as pd

def check_data(file_path='../data/earthquakes-projected.parq'):
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