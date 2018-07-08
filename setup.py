import os
import sys

try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

import param.version

setup_args = dict(
    name='pyviz',
    version=param.version.get_setup_version(__file__,'pyviz',archive_commit="$Format:%h$"),
    description='How to solve visualization problems with Python tools.',
    long_description=open('README.rst').read() if os.path.isfile('README.rst') else 'Consult README.rst',
    author= "PyViz developers",
    author_email= " developers@pyviz.org",
    maintainer="PyViz developers",
    maintainer_email=" developers@pyviz.org",
    entry_points = {
        'console_scripts': ['pyviz=pyviz.cmd:main'],
    },
    packages = ["pyviz"],
    package_data={'pyviz': ['*.yml']},
    platforms=['Windows', 'Mac OS X', 'Linux'],
    license='BSD',
    url='http://pyviz.org',
    classifiers = [
        "License :: OSI Approved :: BSD License",
        "Development Status :: 5 - Production/Stable",
        "Programming Language :: Python :: 2",
        "Programming Language :: Python :: 2.6",
        "Programming Language :: Python :: 2.7",
        "Programming Language :: Python :: 3.2",
        "Programming Language :: Python :: 3.3",
        "Programming Language :: Python :: 3.4",
        "Programming Language :: Python :: 3.5",
        "Programming Language :: Python :: 3.6",
        "Operating System :: OS Independent",
        "Intended Audience :: Science/Research",
        "Intended Audience :: Developers",
        "Natural Language :: English",
        "Topic :: Scientific/Engineering",
        "Topic :: Software Development :: Libraries"]
)


if __name__=="__main__":
    setup(**setup_args)
