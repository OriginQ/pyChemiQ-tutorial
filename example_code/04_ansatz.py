from pychemiq import Molecules,ChemiQ,QMachineType
from pychemiq.Transform.Mapping import jordan_wigner,MappingType
from pychemiq.Optimizer import vqe_solver
from pychemiq.Circuit.Ansatz import UCC,HardwareEfficient,SymmetryPreserved
import numpy as np

multiplicity = 1
charge = 0
basis =  "sto-3g"
geom = ["Li     0.00000000    0.00000000    0.37770300",
        "H      0.00000000    0.00000000   -1.13310900"]
active = [2,2]
mol = Molecules(
    geometry = geom,
    basis    = basis,
    multiplicity = multiplicity,
    charge = charge)
fermion_LiH = mol.get_molecular_hamiltonian()
pauli_LiH = jordan_wigner(fermion_LiH)

chemiq = ChemiQ()
machine_type = QMachineType.CPU_SINGLE_THREAD
mapping_type = MappingType.Jordan_Wigner
pauli_size = len(pauli_LiH.data())
n_qubits = mol.n_qubits
n_elec = mol.n_electrons
chemiq.prepare_vqe(machine_type,mapping_type,n_elec,pauli_size,n_qubits)

# 设置优化器和初始参数
opt_method = "SLSQP"
np.random.seed(20241225)


# 设置ansatz拟设类型，这里使用的是几种不同的拟设
# UCCSD类型的拟设
ucc_ansatz = ["UCCSD", "UCCS", "UCCD"]
for ucc_type in ucc_ansatz:
    ansatz = UCC(ucc_type,n_elec,mapping_type,chemiq=chemiq)
    init_para = np.random.random(ansatz.get_para_num())
    solver = vqe_solver(
            method = opt_method,
            pauli = pauli_LiH,
            chemiq = chemiq,
            ansatz = ansatz,
            init_para=init_para)
    result = solver.fun_val
    print(f"The result of {ucc_type} ansatz is", result)

# 其他拟设类型
ansatz_HE = HardwareEfficient(n_elec,chemiq = chemiq)
ansatz_SP = SymmetryPreserved(n_elec,chemiq = chemiq)
for ansatz in [ansatz_HE, ansatz_SP]:
    init_para = np.random.random(ansatz.get_para_num())
    solver = vqe_solver(
            method = opt_method,
            pauli = pauli_LiH,
            chemiq = chemiq,
            ansatz = ansatz,
            init_para=init_para)
    result = solver.fun_val
    print(f"The result of ansatz is", result)

