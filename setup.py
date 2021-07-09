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
          "prosci": "lib/python/prosci",
          "prosci.loops": "lib/python/prosci/loops",
          "prosci.util": "lib/python/prosci/util",
          "prosci.cpp":"lib/python/prosci/cpp",# Entire protocol as a master script
      },
      scripts = ["bin/esst.txt", "bin/esst.txt", "bin/fread_db_add", "bin/fread_db_optimise", "bin/multifread",
                 "bin/multifread.orig", "bin/pyfread", "bin/pyfread_cpp/", "bin/tools/", "bin/pyfread_cpp/"],
)
