import os
import sys

from setuptools import setup, find_packages

setup_args = dict(
    name='pyviz',
    version=os.environ.get('VERSIONHACK',"0.9.1"),
    description='How to solve visualization problems with Python tools.',
    long_description=open('README.rst').read() if os.path.isfile('README.rst') else 'Consult README.rst',
    author= "PyViz developers",
    author_email= "developers@pyviz.org",
    maintainer="PyViz developers",
    maintainer_email=" developers@pyviz.org",
    platforms=['Windows', 'Mac OS X', 'Linux'],
    license='BSD',
    packages=find_packages(),
    package_data={'pyviz':'datasets.yml'},
    include_package_data=True,
    entry_points = {
        'console_scripts': ['pyviz=pyviz.cmd:main'],
    },
    url='http://pyviz.org',
    classifiers = [
        "License :: OSI Approved :: BSD License",
        "Development Status :: 5 - Production/Stable",
        "Programming Language :: Python :: 2.7",
        "Programming Language :: Python :: 3.6",
        "Operating System :: OS Independent",
        "Intended Audience :: Science/Research",
        "Natural Language :: English",
        "Topic :: Scientific/Engineering"
    ],
    python_requires = ">=2.7",
    install_requires = [
        'holoviews',
        'geoviews',
        'pandas',
        'xarray',
        'colorcet',
        'datashader >=0.6.5',
        'param',
        'parambokeh',
        'numpy',
        'bokeh ==0.12.14',        
        ####################################################################
        # control over dependencies of our dependencies,
        # (e.g. optional dependencies of our dependencies, or if we
        # need particular versions)
        'fastparquet',
        'python-snappy',
        'ipywidgets >=6,<7',
        'cffi',
    ],
    tests_require = [
        # earlier one is failing to install on windows
        'pytest >=3.2'
    ],
    extras_require = {
        'examples': [
            'notebook >=5.1',
            'matplotlib',
            'paramnb',
            'parambokeh',
            'networkx',
            'streamz ==0.2.0',
            'dask ==0.15.4',
            'geopandas',
            'scikit-image'
        ],
        'export_png' : [
            'selenium',
            'phantomjs',
        ]
    }
)


if __name__=="__main__":
    setup(**setup_args)
