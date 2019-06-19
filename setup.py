from setuptools import setup
import os, sys, shutil

import pyct.build

if __name__=="__main__":
    # TODO: hope to eliminate the examples handling from here
    # (i.e. all lines except setup()), moving it to pyct
    example_path = os.path.join(os.path.dirname(os.path.abspath(__file__)),
                                'holoviz','examples')
    if 'develop' not in sys.argv:
        pyct.build.examples(example_path, __file__, force=True)

    setup()

    if os.path.isdir(example_path):
        shutil.rmtree(example_path)
