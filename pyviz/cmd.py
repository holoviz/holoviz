import os
import argparse

def download_sample_data(args):
    import pyviz.download_sample_data
    pyviz.download_sample_data.main(args.destination)

def _cheap_dl_ex(remotezip,dest):
    import io, zipfile
    try:    from urllib.request import urlopen
    except: from urllib import urlopen
    zipfile.ZipFile(io.BytesIO(urlopen(remotezip).read())).extractall(dest)

def download_examples(args):
    for e in examples:
        _cheap_dl_ex(e,args.destination)

_cmds = {
    "download_sample_data": download_sample_data,
    "download_examples": download_examples
}

examples = ["https://www.dropbox.com/s/ry07vd2nu8r6cnm/apps.zip?dl=1",
            "https://www.dropbox.com/s/0npkqd2y90tm7py/notebooks.zip?dl=1"]

def main():
    parser = argparse.ArgumentParser(prog='pyviz')
    parser.add_argument('action', type=str, choices=_cmds.keys(),
                        help='Command to run')
    parser.add_argument('--destination', type=str, default='.',
                        help='Location to store requested download.')
    args = parser.parse_args()
    os.makedirs(args.destination,exist_ok=True)
    _cmds[args.action](args)
