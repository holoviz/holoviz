description = """
Command line interface for pyviz.

This utility makes the pyviz examples available in the current directory
and downloads the required sample data.

The pyviz command supports the following options:
"""

epilog="""
Example usage
-------------

$ pyviz --install-examples pyviz-examples

This will place the examples in the 'pyviz-examples' directory.

$ pyviz --download-sample-data data

This will download the sample data to the 'data' directory.
"""


import os
import sys
import argparse
from argparse import RawTextHelpFormatter

import io, zipfile
try:    from urllib.request import urlopen
except: from urllib import urlopen

from pyviz import download_sample_data



# Note: make sure to included trailing / to indicate directories!
example_assets = ['README.rst',
                  'apps/',
                  'data/',
                  'datasets.yml',
                  'exercises/',
                  'images/',
                  'notebooks/']

def install_examples(path, ref='master'):

    if os.path.exists(path):
        print('%s directory already exists; overwriting current files' % path)

    archive_url = 'https://github.com/pyviz/pyviz/archive/{ref}.zip'.format(ref=ref)
    print('Downloading archive: %r' % archive_url)
    response = urlopen(archive_url)
    print('Download complete. Extracting')
    zf = zipfile.ZipFile(io.BytesIO(response.read()))
    ref = ref[1:] if ref.startswith('v') else ref
    file_assets = ['pyviz-{ref}/{asset}'.format(ref=ref, asset=asset)
                   for asset in example_assets if not asset.endswith('/')]
    dir_assets = []
    for dir_asset in [asset for asset in example_assets if asset.endswith('/')]:
        target = 'pyviz-{ref}/{dir_asset}'.format(ref=ref, dir_asset=dir_asset)
        dir_assets.extend([f.filename for f in zf.filelist
                           if (f.filename.startswith(target)
                               and not f.filename.endswith('/'))])

    for file_path in file_assets + dir_assets:
        file_data = zf.read('{file_path}'.format(ref=ref, file_path=file_path))
        root_dir =  os.path.abspath(os.path.join('.', path))
        raised_path = file_path.replace('pyviz-{ref}/'.format(ref=ref), '')
        filename = os.path.join( root_dir, raised_path)
        os.makedirs(os.path.split(filename)[0], exist_ok=True)
        with open(filename, 'wb') as f:
            f.write(file_data)

def main():
    if len(sys.argv) < 2:
        print("For help with the pyviz command run:\n\npyviz --help\n")
        sys.exit()

    parser = argparse.ArgumentParser(prog='pyviz',
                                     formatter_class=RawTextHelpFormatter,
                                     description=description,
                                     epilog=epilog)

    parser.add_argument('--download-sample-data', metavar='sample_data_dest',
                        const="data",
                        type=str, nargs='?', help='Command to download the sample data.')

    parser.add_argument('--install-examples', metavar='install_examples',
                        const='pyviz_examples',
                        type=str, nargs='?',
                        help='Install examples to the specified directory.')

    args = parser.parse_args()

    if args.download_sample_data:
        download_sample_data.main(args.download_sample_data)
    elif args.install_examples:
        install_examples(args.install_examples)

if __name__ == '__main__':
    main()
