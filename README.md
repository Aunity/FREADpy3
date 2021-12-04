## FREADpy3: A python3 version of FREAD
#=-

* Descriptopm
  FREAD is a database search loop structure prediction protocol. Its primary use is to fill in the gaps in incomplete 3D models of protein structures. Loops are generally located on the protein’s surface and their structures are known to be notoriously difficult to predict. The basic assumption of FREAD is that loops with similar sequences also have similar conformations, taking into account the spatial constraints introduced by their anchor residues (the residues on either side of the loop region).

* software
  FREAD local [download](!http://opig.stats.ox.ac.uk/webapps/sites/fread/index.html)
  FREAD py2 [download](!http://opig.stats.ox.ac.uk/webapps/newsabdab/sabpred/fread/)

* FREADpy3 usage:
    git clone  
    cd FREADpy3
    python setup.py install
    pyfread -h

* Reference
  [Choi, Y. and Deane, C. M. FREAD revisited: accurate loop structure prediction using a database search algorithm. Proteins. (2009).](!https://doi.org/10.1002/prot.22658)

