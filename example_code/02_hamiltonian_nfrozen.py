from pychemiq import Molecules

multiplicity = 1
charge = 0
basis =  "sto-3g"
geom = ["Li     0.00000000    0.00000000    0.37770300",
        "H      0.00000000    0.00000000   -1.13310900"]
nfrozen = 1
mol = Molecules(
    geometry = geom,
    basis    = basis,
    multiplicity = multiplicity,
    charge = charge,
    nfrozen = nfrozen)
fermion_LiH = mol.get_molecular_hamiltonian()
print(fermion_LiH)