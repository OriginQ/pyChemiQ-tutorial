from pychemiq.Transform.Mapping import (jordan_wigner,bravyi_kitaev,parity,segment_parity)

# 先初始化得到氢分子的费米子Hamiltonian
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

# 使用JW变换将得到的氢分子的费米子Hamiltonian映射成泡利形式
pauli_H2 = jordan_wigner(fermion_H2)
print(pauli_H2)



