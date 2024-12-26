# 先导入需要用到的包
from pychemiq import Molecules,ChemiQ,QMachineType
from pychemiq.Transform.Mapping import jordan_wigner,MappingType
from pychemiq.Optimizer import vqe_solver
from pychemiq.Circuit.Ansatz import UCC
import numpy as np

def loss3(para,grad):
    new_para[:] = para[:]
    global result
    result = chemiq.getExpectationValue(0,0,0,chemiq.qvec,H,new_para,ansatz,False)
    if len(grad) == len(para):
        for i in range(len(para)):
            new_para[i] += delta_p
            result_p = chemiq.getExpectationValue(0,0,0,chemiq.qvec,H,new_para,ansatz,False)
            grad[i] = (result_p - result)/delta_p
            new_para[i] -= delta_p
    return result
def GradientDescent():
    para_num = ansatz.get_para_num()
    seed = 20221115
    np.random.seed(seed)
    para = np.zeros(para_num)
    grad = np.zeros(para_num)
    lr = 0.1
    result_previous = 0
    result = 0
    threshold = 1e-8
    for i in range(1000):
        result_previous = result
        result = loss3(para,grad)
        para -= lr*grad
        if abs(result - result_previous) < threshold:
            print("final_energy :",result)
            print("iterations :",i+1)
            break


# 初始化氢分子的电子结构参数，包括电荷、基组、原子坐标(angstrom)、自旋多重度
multiplicity = 1
charge = 0
basis =  "sto-3g"
geom = "H 0 0 0,H 0 0 0.74"

mol = Molecules(
    geometry = geom,
    basis    = basis,
    multiplicity = multiplicity,
    charge = charge)

# 利用JW变换得到泡利算符形式的氢分子哈密顿量
fermion_H2 = mol.get_molecular_hamiltonian()
pauli_H2 = jordan_wigner(fermion_H2)

# 准备量子线路，需要指定的参数有量子虚拟机类型machine_type，拟设映射类型mapping_type，
# 泡利哈密顿量的项数pauli_size，电子数目n_elec与量子比特的数目n_qubits
chemiq = ChemiQ()
machine_type = QMachineType.CPU_SINGLE_THREAD
mapping_type = MappingType.Jordan_Wigner
pauli_size = len(pauli_H2.data())
n_qubits = mol.n_qubits
n_elec = mol.n_electrons
chemiq.prepare_vqe(machine_type,mapping_type,n_elec,pauli_size,n_qubits)

# 设置拟设类型，这里我们使用UCCSD拟设
ansatz = UCC("UCCSD",n_elec,mapping_type,chemiq=chemiq)


# 指定loss函数中的泡利哈密顿量H和参数delta_p，以及初始参数new_para
new_para = np.zeros(ansatz.get_para_num())
delta_p = 1e-3
H = pauli_H2.to_hamiltonian(True)
GradientDescent()
