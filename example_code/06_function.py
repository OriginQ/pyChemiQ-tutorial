# 导入所需的包
from pychemiq import Molecules,ChemiQ,QMachineType
from pychemiq.Transform.Mapping import jordan_wigner,MappingType
from pychemiq.Optimizer import vqe_solver
from pychemiq.Circuit.Ansatz import UCC
import numpy as np
from pyscf import gto, scf, fci
import matplotlib.pyplot as plt

# 进行势能面扫描：先初始化参数，再构建不同键长下的分子体系，进行多次单点能计算
basis = 'sto-3g'
multiplicity = 1
charge=0

## 定义步长间隔、步数
bond_length_interval = 0.1
n_points = 40
bond_lengths = []
energies = []
for point in range(3, n_points + 1):
    bond_length = bond_length_interval * point
    bond_lengths += [bond_length]
    geometry = ["H 0 0 0", f"H 0 0 {bond_length}"]

    mol = Molecules(
        geometry = geometry,
        basis    = basis,
        multiplicity = multiplicity,
        charge = charge)

    fermion_H2 = mol.get_molecular_hamiltonian()
    pauli_H2 = jordan_wigner(fermion_H2)

    chemiq = ChemiQ()
    machine_type = QMachineType.CPU_SINGLE_THREAD
    mapping_type = MappingType.Jordan_Wigner
    pauli_size = len(pauli_H2.data())
    n_qubits = mol.n_qubits
    n_elec = mol.n_electrons
    chemiq.prepare_vqe(machine_type,mapping_type,n_elec,pauli_size,n_qubits)
    ansatz = UCC("UCCSD",n_elec,mapping_type,chemiq=chemiq)

    method = "SLSQP"
    init_para = np.zeros(ansatz.get_para_num())
    solver = vqe_solver(
            method = method,
            pauli = pauli_H2,
            chemiq = chemiq,
            ansatz = ansatz,
            init_para=init_para)
    energy = solver.fun_val
    energies += [energy]

# 使用经典计算化学软件PySCF的FCI方法来计算氢分子在不同键长下的能量
pyscf_energies = []
bond_length_interval = 0.1
n_points = 40
for point in range(3, n_points + 1):
    bond_length = bond_length_interval * point
    atom = f'H 0 0 0; H 0 0 {bond_length}'

    mol = gto.M(atom=atom,   # in Angstrom
            basis='STO-3G',
            charge=0,
            spin=0)
    myhf = scf.HF(mol).run()
    cisolver = fci.FCI(myhf)
    pyscf_energies += [cisolver.kernel()[0]]


# 最后我们使用matplotlib来绘制氢分子势能面
plt.figure()
plt.plot(bond_lengths, energies, '-g',label='pyChemiQ')
plt.plot(bond_lengths, pyscf_energies, '--r',label='PySCF')
plt.ylabel('Energy in Hartree')
plt.xlabel('Bond length in angstrom')
plt.legend()
plt.show()