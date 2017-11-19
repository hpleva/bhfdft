class Atom(object):
    """Represents an atom whose electronic structure we want to solve.

        Parameters:

        Z: int
            The atomic number of the atom.
        method: str
            Name of the solution method, HF or DFT.
        XC: str
            The flavor of XC that should be used in a DFT calculation.
        rel: bool
            True for a relativistic calculation, False for non-relativistic.
    """
    def __init__(self, Z=1, method='DFT', XC='LDA', rel=False):
        self.Z = Z
        self.method = method
        self.XC = XC
        self.rel = rel
