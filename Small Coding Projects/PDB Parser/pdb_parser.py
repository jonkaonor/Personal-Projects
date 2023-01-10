"""
Code for PDB file parsing and manipulation 
PDB File Example:
COMPND AMMONIA
ATOM 1 N 0.257 -0.363 0.000
ATOM 2 H 0.257 0.727 0.000
ATOM 3 H 0.771 -0.727 0.890
ATOM 4 H 0.771 -0.727 -0.890
END
"""

class Atom :
    """An atom with an index number, the element symbol, and the x, y, z coordinates """s
    def __init__(self, index, element_symbol, x_coord, y_coord, z_coord) :
        self.index = index
        self.element_symbol = element_symbol 
        self.x_coord = x_coord
        self.y_coord = y_coord
        self.z_coord = z_coord 

    def __str__(self) -> str:
        """
        Returns a string representation of Atom
        """
    
    def __repr__(self) :
        """"""
    
    def translate(x, y, z) :
        """"""

class Molecule:
    def __init__(self, atom_list) :
        self.atom_list = atom_list 
