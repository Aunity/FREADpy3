#!/usr/bin/python
# -*- coding: utf-8 -*-

import sys
import os.path
import subprocess
from prosci.util.pdb import Pdb
from prosci.common import NotFoundError

def get_pdb_path(pdb_code, pdb_dir):
  pdb_code = pdb_code.lower()
  return os.path.normpath(pdb_dir)+'/'+pdb_code[1:3]+'/pdb'+pdb_code+'.ent.gz'

def get_pdb_file(pdb_code, pdb_dir):
  stringpath = get_pdb_path(pdb_code, pdb_dir)
  if os.path.isfile(stringpath):
    return subprocess.Popen("gunzip -c "+stringpath, shell=True, stdout=subprocess.PIPE).stdout
  return None

def getpdb(pdb_code, pdb_dir):
  openfile = get_pdb_file(pdb_code, pdb_dir)
  if openfile is None:
    raise NotFoundError("PDB file '%s' not found in database dir '%s'"%(pdb_code, pdb_dir))
  return Pdb(pdb_code, openfile)

get_pdb = getpdb
