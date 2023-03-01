# -*- coding: UTF-8 -*-
from pychemiq import Mole 
import numpy as np

class Molecules(Mole):
    """
    Docstrings for class Molecules
    geometry: atom types and atom coordinates
        geometry = "H 0 0 0,H 0 0 0.74" or 
        geometry = [
            "H 0 0 0",
            "H 0 0 0.74"
        ]
    """
    def __init__(self, 
        geometry=None,
        basis=None,
        multiplicity=None,
        charge=0,
        active = None,
        nfrozen = None,
        filename="",
        directory=None):

        if type(geometry) == type([]):
            geometry = ",".join(geometry)
        if active == None:
            active = [0,0]
        if nfrozen == None:
            nfrozen = 0
        self.geometry     = geometry
        self.basis        = basis
        self.multiplicity = multiplicity
        self.charge       = charge
        if geometry == None:
            self.argPrintError("geometry")
            return 
        if basis == None:
            self.argPrintError("basis")
            return
        if multiplicity == None:
            self.argPrintError("multiplicity")
            return

        bohr = False
        pure = False

        Mole.__init__(self,geometry,basis,charge,multiplicity,bohr,pure,"","rectangular")
        # setting active space
        if nfrozen == 0:
            self.setActiveSpace(active)
        else:
            self.setActiveSpace([0,-1])
            self.setNfrozen(nfrozen)
        hf_iters = 1000 
        hf_threshold = 1e-10
        self.HF(hf_iters,hf_threshold) 
        self.molecular_hamiltonian = self.getHamiltonian()
        self.getAttributes()  
          
        return
    def getAttributes(self):
        """
        Docstrings for method getAttributes
        """

        self.n_atoms = self.getnatom()
        self.n_electrons = self.getElectronNum()
        self.hf_energy = self.getEhf()
        self.nuclear_repulsion = self.getEnuc()
        self.canonical_orbitals = self.getMolecularOrbitals()
        self.n_orbitals = self.getnmo()
        self.n_qubits   = 2*self.getnmo()
        self.orbital_energies = self.getOrbitalEnergies()
        self.overlap_integrals = self.getOverlapMatrix()
        self.one_body_integrals = self.getA()
        self.two_body_integrals = self.getGFromMatrix()
        return

    def getGFromMatrix(self):
        """
        Docstrings for method getG
        """
        G = self.getDoubleIntegrals()
        # number of basis functions
        n = self.one_body_integrals.shape[0]
        G = G.reshape((n,n,n,n))
        return G 
    
    def argPrintError(self,err):
        """
        Docstrings for method printError
        """
        print(f"ERROR: Please input {err}!!!!")
        return
    def get_molecular_hamiltonian(self):
        """
        Docstrings for method get_molecular_hamiltonian
        """
        return self.molecular_hamiltonian

    def get_active_space_integrals(self,active_orbitals=None, active_electrons=None):
        """
        Docstrings for method get_active_space_integrals
        """
        
        return
