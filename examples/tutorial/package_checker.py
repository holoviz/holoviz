import pathlib
import sys

try:
    import tomllib
except ModuleNotFoundError:
    import tomli as tomllib

from packaging.version import Version
from packaging.specifiers import SpecifierSet


def get_required_versions(toml_path):
    """
    Reads the pixi.toml configuration and extracts package version requirements.

    Returns:
        dict: A dictionary mapping package names to their version specifier strings.
    """
    toml_file_path = pathlib.Path(toml_path)
    with open(toml_file_path, 'rb') as file:
        data = tomllib.load(file)
    dependencies = data.get('dependencies', {})
    version_dict = {}
    for pkg, version_spec in dependencies.items():
        if version_spec and version_spec != '*':
            version_dict[pkg] = version_spec
    return version_dict


def check_packages(packages, toml_path='../pixi.toml'):
    """
    Checks if specified packages are installed with correct versions as per the pixi.toml configuration.

    Args:
        packages (list): A list of package names to check.
    """
    required_versions = get_required_versions(toml_path)
    error_found = False
    for pkg in packages:
        try:
            version_spec = required_versions.get(pkg)
            installed_version = sys.modules[pkg].__version__
            if version_spec:
                specifier = SpecifierSet(version_spec.replace(".*", ""))
                if installed_version not in specifier:
                    print(f"Error: {pkg} version {installed_version} does not satisfy {version_spec}")
                    error_found = True
        except (KeyError, AttributeError):
            print(f"{pkg} is not installed or not specified in the configuration.")
            error_found = True

    if not error_found:
        print("All specified packages are correctly installed.")
