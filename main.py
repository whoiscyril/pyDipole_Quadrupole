from Cell import Cell
from Atom import Atom
import sys

if __name__ == '__main__':
    if len(sys.argv) > 1:
        filename = sys.argv[1]
    else:
        filename = 'input.gin'
    cell = Cell(filename)
    atom_list = cell.atoms_frac
    for atom in cell.atoms_frac:
        print(
            f"ID: {atom.id}, Label: {atom.label}, Type: {atom.type}, Coordinates: ({atom.x}, "
            f"{atom.y}, {atom.z}), Charge: {atom.q}")
