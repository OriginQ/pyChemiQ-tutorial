from pychemiq import Molecules,ChemiQ,QMachineType
from pychemiq.Transform.Mapping import bravyi_kitaev,MappingType
from pychemiq.Optimizer import vqe_solver
from pychemiq.Circuit.Ansatz import UCC
import numpy as np

# 初始化分子的电子结构参数，包括电荷、基组、原子坐标、自旋多重度、活性空间
multiplicity = 1
charge = 0
basis =  "sto-3g"
geom = ["O      0.00000000    0.00000000    0.12713100",
        "H      0.00000000    0.75801600   -0.50852400",
        "H      0.00000000   -0.75801600   -0.50852400"]
active = [4,4]

mol = Molecules(
    geometry = geom,
    basis    = basis,
    multiplicity = multiplicity,
    charge = charge,
    active = active)

# 通过BK变换得到泡利算符形式的水分子哈密顿量并打印结果
fermion_H2O = mol.get_molecular_hamiltonian()
pauli_H2O = bravyi_kitaev(fermion_H2O)
print(pauli_H2O)

# 准备量子线路，需要指定的参数有量子虚拟机类型machine_type，拟设映射类型mapping_type，
# 泡利哈密顿量的项数pauli_size，电子数目n_elec与量子比特的数目n_qubits
chemiq = ChemiQ()
machine_type = QMachineType.CPU_SINGLE_THREAD
mapping_type = MappingType.Bravyi_Kitaev
pauli_size = len(pauli_H2O.data())
n_qubits = mol.n_qubits
n_elec = mol.n_electrons
chemiq.prepare_vqe(machine_type,mapping_type,n_elec,pauli_size,n_qubits)

# 设置簇算符需要的映射方法及簇算符类型，这里我们使用UCCSD拟设
ansatz = UCC("UCCSD",n_elec,mapping_type,chemiq=chemiq)

# 指定经典优化器与初始参数并迭代求解
method = "L-BFGS-B"
init_para = np.zeros(ansatz.get_para_num())
solver = vqe_solver(
    method = method,
    pauli = pauli_H2O,
    chemiq = chemiq,
    ansatz = ansatz,
    init_para=init_para)
result = solver.fun_val
n_calls = solver.fcalls
print(result,f"函数共调用{n_calls}次")

energies = chemiq.get_energy_history()
print(energies)