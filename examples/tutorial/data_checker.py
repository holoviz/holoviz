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
        source = pathlib.Path("/shared/scipy/hvplot-and-panel")
        dest = pathlib.Path("../data")
        data_path = dest / "earthquakes-projected.parq"
        if source.exists() and not data_path.exists():
            for path in source.glob("*"):
                linked_path = dest / path.name
                print(f"Adding symlink to data file: {str(path)} -> {str(linked_path)}")
                linked_path.symlink_to(path, target_is_directory=path.is_dir())
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
