import pathlib
import pandas as pd
import os

def check_data(file_path='../data/earthquakes-projected.parq'):
    """
    Checks if the data file exists and reads it.

    Args:
        file_path (str, optional): The path to the parquet file. Default is '../data/earthquakes-projected.parq'.

    """
    path = pathlib.Path(file_path)

    # Hack to make Nebari installation work for SciPy 2024; can be deleted after the conference
    try:
        source = "/shared/scipy/hvplot-and-panel"
        dest = "../data"
        if os.path.exists(source) and not os.path.exists(dest):
            print(f"Adding symlink to data files: {str(dest)} -> {str(source)}")
            os.symlink(source, dest)

    except RuntimeError as e:
        print(f"Encountered exception during SciPy/Nebari setup: {str(e)}")

    # Try to read the file
    if not path.is_file():
        print(f"Data file does not exist at {file_path}")

    try:
        columns = ['depth', 'id', 'latitude', 'longitude', 'mag', 'place', 'time', 'type']
        data = pd.read_parquet(path, columns=columns, engine='pyarrow')
        data.head()
        print("Data exists and is readable!")
    except RuntimeError as e:
        print(f"The data cannot be read: {str(e)}")
