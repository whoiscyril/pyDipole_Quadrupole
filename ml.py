from Atom import Atom
class ML:
    def __init__(self, filename):
        self.filename = filename
        self.r1atoms_before = []
        self.r2atoms_before = []
        self.atoms_before = []
        self.r1atoms_after = []
        self.r2atoms_after = []
        self.atoms_after = []
        self.r1size = 0.
        self.r2size = 0.
        self.centre = []
    def get_r2atoms_before(self):
        with open(self.filename) as f:
            for line in f:
                if line.startswith("  Region 2 :"):
                    for _ in range(5):
                        line = f.readline()
                    ctn = 1
                    while True:
                        line = f.readline()
                        if line.startswith("---"):
                            break
                        atom = Atom()
                        atom.id = ctn
                        atom.label = line.strip().split()[1]
                        atom.type = line.strip().split()[2]
                        atom.x = float(line.strip().split()[3])
                        atom.y = float(line.strip().split()[4])
                        atom.z = float(line.strip().split()[5])
                        atom.q = float(line.strip().split()[6])
                        self.r2atoms_before.append(atom)
                        ctn += 1
        return self.r2atoms_before
    def get_r1atoms_before(self):
        with open(self.filename) as f:
            for line in f:
                if line.startswith("  Region 1 (Absolute coordinates) :"):
                    for _ in range(5):
                        line = f.readline()
                    ctn = 1
                    while True:
                        line = f.readline()
                        if line.startswith("---"):
                            break
                        atom = Atom()
                        atom.id = ctn
                        atom.label = line.strip().split()[1]
                        atom.type = line.strip().split()[2]
                        atom.x = float(line.strip().split()[3])
                        atom.y = float(line.strip().split()[5])
                        atom.z = float(line.strip().split()[7])
                        atom.q = float(line.strip().split()[9])
                        self.r1atoms_before.append(atom)
                        ctn += 1
        return self.r1atoms_before



    def get_defect_centre(self):
        with open(self.filename) as f:
            for line in f:
                if line.startswith("centre"):
                    parts = line.split()
                    self.centre = list(map(float, parts[-3:]))
        return self.centre

    def get_region_size(self):
        with open(self.filename) as f:
            for line in f:
                if line.startswith("size"):
                    parts = line.split()
                    self.r1size, self.r2size = parts[1:]
        return self.r1size, self.r2size

    def get_r12a(self):
        with open(self.filename) as f:
            for line in f:
                if line.startswith("region_1"):
                    ctn = 1
                    while True:
                        line = f.readline()
                        if len(line.split()) < 5:
                            break
                        else:
                            atom = Atom()
                            atom.id = ctn
                            atom.label = line.strip().split()[0]
                            atom.type = line.strip().split()[1]
                            atom.x = float(line.strip().split()[2])
                            atom.y = float(line.strip().split()[3])
                            atom.z = float(line.strip().split()[4])
                            atom.q = float(line.strip().split()[5])
                            self.atoms_after.append(atom)
                            ctn += 1
        return self.atoms_after








