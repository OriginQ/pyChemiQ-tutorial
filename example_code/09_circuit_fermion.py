from pychemiq import FermionOperator

a = FermionOperator("3+ 2+ 1 0", 1)
print(a)

from pychemiq.Utils import get_cc_n_term,get_cc
import numpy as np
n_para = get_cc_n_term(4,2,"CCD")
para = np.ones(n_para)
cc_fermion = get_cc(4,2,para,"CCD")
print(cc_fermion)

# 以氢分子为例, 将得到的激发费米子算符输入到UserDefine函数中的fermion参数
from pychemiq import Molecules,ChemiQ,QMachineType,FermionOperator
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

# 使用自定义量子线路，将自定义的激发费米子算符输入到fermion参数中
a = FermionOperator("3+ 2+ 1 0", 1)
ansatz = UserDefine(n_elec, fermion=a, chemiq=chemiq)

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