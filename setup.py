#!/usr/bin/env python

from setuptools import setup
import numpy as np

numpy_include_dir = np.get_include()

# Setup script written by Jinwoo Leem
# Modified by Maohua Yang

setup(
        name = 'pyfread',
        version = '1.5',
        description = "FREAD: fragment-based loop modelling method",
        author='Sebastian Kelm',
        author_email = "kelm@stats.ox.ac.uk",
        url='http://opig.stats.ox.ac.uk/webapps/newsabdab/sabpred/fread/',
        packages = [
          "pyfread",                    # Entire module
          "pyfread.loops",
          "pyfread.util",
          "pyfread.cpp"
        ],
        package_dir = {
          "pyfread": "pyfread",
          "pyfread.loops": "pyfread/loops",
          "pyfread.util": "pyfread/util",
          "pyfread.cpp":"pyfread/cpp",# Entire protocol as a master script
      },
      scripts = [ "pyfread/bin/esst.txt", "pyfread/bin/fread_db_add", "pyfread/bin/fread_db_optimise", "pyfread/bin/multifread",
                 "pyfread/bin/multifread.orig", "pyfread/bin/pyfread" ],
)
