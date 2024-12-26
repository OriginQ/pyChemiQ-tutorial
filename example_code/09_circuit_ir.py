from pychemiq import Molecules,ChemiQ,QMachineType
from pychemiq.Transform.Mapping import jordan_wigner,MappingType
from pychemiq.Optimizer import vqe_solver
from pychemiq.Circuit.Ansatz import UserDefine
import numpy as np

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
pauli_H2 = jordan_wigner(fermion_H2)

chemiq = ChemiQ()
machine_type = QMachineType.CPU_SINGLE_THREAD
mapping_type = MappingType.Jordan_Wigner
pauli_size = len(pauli_H2.data())
n_qubits = mol.n_qubits
n_elec = mol.n_electrons
chemiq.prepare_vqe(machine_type,mapping_type,n_elec,pauli_size,n_qubits)

# 使用自定义量子线路，将originIR格式的字符串输入到circuit参数中
circuit = """
    X q[0]
    X q[1]
    BARRIER q[2]
    BARRIER q[3]
    H q[0]
    H q[1]
    H q[2]
    RX q[3],(-1.5707963)
    CNOT q[0],q[3]
    CNOT q[1],q[3]
    CNOT q[2],q[3]
    RZ q[3],(0.785398)
    CNOT q[2],q[3]
    CNOT q[1],q[3]
    CNOT q[0],q[3]
    H q[0]
    H q[1]
    H q[2]
    RX q[3],(1.5707963)
"""
ansatz = UserDefine(n_elec, circuit=circuit, chemiq=chemiq)

# 最后指定经典优化器与初始参数并迭代求解
method = "SLSQP"
init_para = np.zeros(ansatz.get_para_num())
solver = vqe_solver(
        method = method,
        pauli = pauli_H2,
        chemiq = chemiq,
        ansatz = ansatz,
        init_para=init_para)
result = solver.fun_val
print(result)