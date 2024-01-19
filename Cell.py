from Atom import Atom


class Cell:
    def __init__(self, filename):
        self.filename = filename
        self.a = 0.
        self.b = 0.
        self.c = 0.
        self.alpha = 0.
        self.beta = 0.
        self.gamma = 0.
        self.atoms_cart = []
        self.atoms_frac = []

        with open(filename) as f:
            for line in f:
                if line.startswith('cell'):
                    line = f.readline()
                    self.a = float(line.strip().split()[0])
                    self.b = float(line.strip().split()[1])
                    self.c = float(line.strip().split()[2])
                    self.alpha = float(line.strip().split()[3])
                    self.beta = float(line.strip().split()[4])
                    self.gamma = float(line.strip().split()[5])
                    ctn = 1
                    for line in f:
                        if line.startswith('frac'):
                            while True:
                                line = f.readline()
                                if len(line.strip().split()) != 6:
                                    break
                                atom = Atom()
                                atom.id = ctn
                                atom.label = line.strip().split()[0]
                                atom.type = line.strip().split()[1]
                                atom.x = float(line.strip().split()[2])
                                atom.y = float(line.strip().split()[3])
                                atom.z = float(line.strip().split()[4])
                                atom.q = float(line.strip().split()[5])
                                self.atoms_frac.append(atom)
                                ctn += 1


    def get_parameters(self):
        with open(self.filename) as f:
            for line in f:
                if line.startswith('cell'):
                    line = f.readline()
                    self.a = float(line.strip().split()[0])
                    self.b = float(line.strip().split()[1])
                    self.c = float(line.strip().split()[2])
                    self.alpha = float(line.strip().split()[3])
                    self.beta = float(line.strip().split()[4])
                    self.gamma = float(line.strip().split()[5])

    def get_atoms_frac(self):
        with open(self.filename) as f:
            ctn = 1
            for line in f:
                if line.startswith('frac'):
                    while True:
                        line = f.readline()
                        if len(line.strip().split()) != 6:
                            break
                        atom = Atom()
                        atom.id = ctn
                        atom.label = line.strip().split()[0]
                        atom.type = line.strip().split()[1]
                        atom.x = float(line.strip().split()[2])
                        atom.y = float(line.strip().split()[3])
                        atom.z = float(line.strip().split()[4])
                        atom.q = float(line.strip().split()[5])
                        self.atoms_frac.append(atom)
                        ctn += 1
