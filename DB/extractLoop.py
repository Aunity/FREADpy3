import os
import sys
import argparse
from MDAnalysis import Universe

def extract_loop(pdbfile, loop, chain='H', outfile=None):
    cutoff = 10
    pdbname =  os.path.split(pdbfile)[-1][:-4]
    if outfile is None:
        outfile = pdbname + "_loop_%s_%d-%d.pdb"%(chain, loop[0], loop[1])
    u = Universe(pdbfile)
    selstr = 'resid %d-%d and segid %s'%(loop[0]-cutoff, loop[1]+cutoff, chain)
    print(pdbfile, loop,selstr)
    loopGroup = u.select_atoms(selstr)
    loopGroup.write(outfile)

def read_file(recordfile, outp=None):
    if outp is None:
        outp = 'loop'
    if not os.path.exists(outp):
            os.mkdir(outp)
    with open(recordfile) as fr:
        for line  in fr:
            if line.startswith('#'):
                continue
            lineList = line.split()
            pdbfile = lineList[0]
            chain = lineList[1]
            loop = list(map(int, lineList[2].split("-")))
            outfile = os.path.join(outp, os.path.split(pdbfile)[-1][:-4]) + ".pdb"
            extract_loop(pdbfile, loop, chain, outfile)

def main():
    parser = argparse.ArgumentParser(description='Extract loop from pdb file.')
    parser.add_argument('-i', dest='inps', nargs='+', help='The input PDB files.', required=True)
    parser.add_argument('-loop', help='RMSD calculate region: start end', nargs=2, type=int, default=None)
    parser.add_argument('-c', dest='chain', help='Chain name of loop region. Default is H', default='H')
    parser.add_argument('-o', dest='outf', help='Outfile name or output directory.', default=None)
    args = parser.parse_args()
    inp, loop, chain, out = args.inps, args.loop, args.chain, args.outf
    if len(inp)==1:
        if inp[0].endswith('.txt'):
            read_file(inp[0], out)
        else:
            extract_loop(inp[0], loop, chain, out)
    else:
        if not os.path.exists(out):
            os.mkdir(out)
        for pdbfile in inp:
            outfile = os.path.join(out, os.path.split(pdbfile)[-1][:-4]) + ".pdb"
            extract_loop(pdbfile, loop, chain, outfile)

if __name__ == "__main__":
    main()
