from Cell import Cell
from Atom import Atom
from ml import ML
import sys

if __name__ == '__main__':
    if len(sys.argv) > 1:
        infile = sys.argv[1]
        outfile = sys.argv[2]
        resfile = sys.argv[3]
    else:
        raise("Not enough files")
    # cell = Cell(filename)
    output = ML(outfile)
    r2atoms = output.get_r2atoms_before()

    for atom in r2atoms:
        print(f"{atom.id}, {atom.label}, {atom.type},{atom.x}, {atom.y}, {atom.z}, {atom.q}")
