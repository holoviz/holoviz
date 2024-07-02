import yaml
import pathlib
import sys
from packaging.version import Version

def get_required_versions(yaml_path):
    """
    Reads the YAML configuration and extracts all package version requirements.
    
    Returns:
        dict: A dictionary mapping package names to their required versions.
    """
    yaml_file_path = pathlib.Path(yaml_path)
    with open(yaml_file_path, 'r') as file:
        data = yaml.safe_load(file)
        packages = data['packages']
        version_dict = {}
        for package in packages:
            for delimiter in ['==', '>=']:
                if delimiter in package:
                    pkg, version = package.split(delimiter)
                    version = version.split(',')[0]
                    version_dict[pkg] = version
                    break
        return version_dict

def check_packages(packages, yaml_path='../anaconda-project.yml'):
    """
    Checks if specified packages are installed with correct versions as per the YAML configuration.
    
    Args:
        packages (list): A list of package names to check.
    """
    required_versions = get_required_versions(yaml_path)
    error_found = False
    for pkg in packages:
        try:
            req_version = required_versions[pkg]
            installed_version = sys.modules[pkg].__version__
            if Version(installed_version) < Version(req_version):
                print(f"Error: {pkg} expected version {req_version}, got {installed_version}")
                error_found = True
        except KeyError:
            print(f"{pkg} is not installed or not specified in the YAML configuration.")
            error_found = True

    if not error_found:
        print("All specified packages are correctly installed.")
