from pychemiq import Molecules

multiplicity = 1
charge = 0
basis =  "sto-3g"
geom = "H 0 0 0,H 0 0 0.74"
mol = Molecules(
    geometry = geom,
    basis    = basis,
    multiplicity = multiplicity,
    charge = charge)

fermion_H2 = mol.get_molecular_hamiltonian()
print(fermion_H2)