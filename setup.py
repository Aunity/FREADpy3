#!/usr/bin/env python

from setuptools import setup
import numpy as np

numpy_include_dir = np.get_include()

# Setup script written by Jinwoo Leem
# Modified by Maohua Yang

setup(
        name = 'prosci',
        version = '1.0',
        description = "FREAD: fragment-based loop modelling method",
        author='Sebastian Kelm',
        author_email = "kelm@stats.ox.ac.uk",
        url='http://opig.stats.ox.ac.uk/webapps/newsabdab/sabpred/fread/',
        packages = [
          "prosci",                    # Entire module
          "prosci.loops",
          "prosci.util",
          "prosci.cpp"
        ],
        package_dir = {
          "prosci": "prosci",
          "prosci.loops": "prosci/loops",
          "prosci.util": "prosci/util",
          "prosci.cpp":"prosci/cpp",# Entire protocol as a master script
      },
      scripts = [ "prosci/bin/esst.txt", "prosci/bin/fread_db_add", "prosci/bin/fread_db_optimise", "prosci/bin/multifread",
                 "prosci/bin/multifread.orig", "prosci/bin/pyfread" ],
)
